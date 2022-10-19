from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class PlayerView(APIView):

    def post(self,request,format=None):
        return Response({},status=status.HTTP_201_CREATED)

    def get(self,request):
        return Response()