from django.core.management.base import BaseCommand
import logging
from django.db import connection

logger = logging.getLogger('my_logger')

class Command(BaseCommand):
    help = 'Read data from weather folder and insert into db'

    def add_arguments(self, parser):
        parser.add_argument('--option', type=str, help='An optional argument')

    def handle(self, *args, **options):
        logger.info("Analysis starting")
        with connection.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM weather_analysis;")
                logger.info("Deleted all old data from weather_analysis")

                cursor.execute("""
                    INSERT INTO weather_analysis (station_id, year, avg_max_temperature, avg_min_temperature, total_precipitation)
                    SELECT
                        station_id,
                        strftime('%Y', date) AS year,  
                        AVG(max_temperature / 10.0) AS avg_max_temp,
                        AVG(min_temperature / 10.0) AS avg_min_temp,
                        SUM(precipitation / 10.0) AS total_precipitation
                    FROM weather_data
                    GROUP BY station_id, year
                """)
                logger.info("Analysis data inserted into weather_analysis table.")

            except Exception as e:
                logger.error("Error during data analysis: %s", e, exc_info=True)
            else:
                logger.info("Data analysis completed successfully.")
