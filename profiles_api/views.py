#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """returns a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, put, patch, delete)',
            'Is similar to traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview})
