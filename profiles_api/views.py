#from django.shortcuts import render
#from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions



class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """returns a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, put, patch, delete)',
            'Is similar to traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handle updating (in a sense replacing the previous info with new info) an object"""
        return Response({'method':'PUT'})
    

    def patch(self, request, pk=None):
        """Handle partially updating an object"""
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API View set"""

    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """Return a Hello Messsage - list a set of objects that the viewset represents"""

        a_viewset=[
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'provides more functionality with less code',
        ]

        return Response({'message':'hello', 'a_viewset':a_viewset})
    
    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def retrieve(self, request, pk=None):
        """Handle getting an object bt its PK"""
        return Response({'http_method':'get'})


    def update(self, request, pk=None):
        """Handle updating (in a sense replacing the previous info with new info) an object"""
        return Response({'http_method':'PUT'})
    

    def partial_update(self, request, pk=None):
        """Handle partially updating an object"""
        return Response({'http_method':'PATCH'})


    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and Updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    Authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)