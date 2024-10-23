from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class Helper():

    def convertSerializerErrors(errors):
        outError = {}
        for fieldName, message in errors.items():
            outError[fieldName] = message[0]
        return outError    
    
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    #max_page_size = 5
    #page_query_param = 'page'
    def get_paginated_response(self, data):
        return Response({
            "status":True,
            "message":"Featched successfully",
            "data": {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'results': data
        }})