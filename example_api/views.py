from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from . import models
from . import permissions

#Create your views here.
class Hello(APIView):

    serializer_class = serializers.HelloSerailizers

    def post(self,request):
        serializer = serializers.HelloSerailizers(data= request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        return Response({'message':'put method'})

    def patch(self,request,pk=None):
        return Response({'message':'patch method'})
    def delete(self,request,pk=None):
        return Response({'message':'delete mehod'})


    def get(self,request,format=None):
        an_apiview = [
            'hello my name is sujjad',
            'i am learing django',
            'django rest framework'
        ]
        return Response({'message':'hello','an_apiview':an_apiview})
class HelloApiViewset(viewsets.ViewSet):
    serializer_class = serializers.HelloSerailizers

    def list(self,request):
        a_viewset = [
            'sujjad is good boy',
            'he is learing django',
            'django rest framework is easy'
        ]
        return Response({'message':'hello sujjad','a_viewset':a_viewset})
    def create(self,request):
        serializer = serializers.HelloSerailizers(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        return Response({'message':'retrieve method'})

    def update(self,request,pk=None):
        return Response({'message':'update method'})

    def partial_update(self,request,pk=None):
        return Response({'message':'partial_update method'})

    def destroy(self,request,pk=None):
        return Response({'message':'destroy method'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class LoginViewSet(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer


    def create(self,request):
            return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedSerializer
    permission_classes = (permissions.PostOwnStatus,IsAuthenticated)
    queryset = models.ProfilesFeedItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)











