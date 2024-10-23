from django.core.management.base import BaseCommand
from datetime import datetime
import logging
import os
logger = logging.getLogger('my_logger')
dataDir = 'wx_data/'
from weather.models import WeatherData
from django.db import transaction



class Command(BaseCommand):
    help = 'Read data from weather folder and insert into db'
 
    def add_arguments(self, parser):
        # Optional: Define command-line arguments
        parser.add_argument('--option', type=str, help='An optional argument')
 
    def handle(self, *args, **options):
        logger.info('Dumping started...')  
        startTime = datetime.now()
        insertCount=0
        for fileName in os.listdir(dataDir):
            if fileName.endswith(".txt"):
                with open(os.path.join(dataDir, fileName), 'r') as file:
                    logger.info('Dumping started for '+fileName + " file")  
                    weatherDataInfo = []
                    for line in file:
                        stationId=fileName.split('.')[0]
                        dateStr, maxTemperature, minTemperature, precipitation = line.strip().split('\t')
                        date = datetime.strptime(dateStr, '%Y%m%d').date()
                        maxTemperature=self.convertMissingValues(maxTemperature)
                        minTemperature=self.convertMissingValues(minTemperature)
                        precipitation=self.convertMissingValues(precipitation)
                        weatherDataInfo.append(WeatherData(
                            station_id=stationId,
                            date=date,
                            max_temperature=maxTemperature,
                            min_temperature=minTemperature,
                            precipitation=precipitation
                            ))
                    with transaction.atomic():
                        innerCut = WeatherData.objects.bulk_create(weatherDataInfo, ignore_conflicts=True)
                        insertCount += len(innerCut)
                        logger.info('Dump completed for '+fileName + " file,total insert count "+str(len(innerCut)))
        endTime = datetime.now()
        logger.info(f"Dump completed in {endTime - startTime} seconds,total insert count"+str(insertCount))


    def convertMissingValues(self,val):
        if val != '-9999':
            val = int(val)
        else:
            val = None
        return val

