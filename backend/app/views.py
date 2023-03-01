from django.shortcuts import render
from .serializers import *
from .data import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,status,views,permissions,viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,UpdateAPIView

class CreateMovie(CreateAPIView):
    serializer_class = Datas
    queryset = Data.objects.all()
    # permission_classes = (permissions.IsAuthenticated,autorisation)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

    def get_queryset(self):
        return self.queryset.filter()
    
class CreateGenre(CreateAPIView):
    serializer_class = Genres
    queryset = genre.objects.all()
    # permission_classes = (permissions.IsAuthenticated,autorisation)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()

    def get_queryset(self):
        return self.queryset.filter()
    


  
@api_view(['GET'])
@csrf_exempt
# @permission_classes([IsAuthenticated,autorisation])	
def ViewallMovie(request):
	serializer_class = DatasView
	donnee = Data.objects.all()
	
	
	serializer = serializer_class(donnee,many=True)
	return Response(serializer.data)
# Create your views here.
