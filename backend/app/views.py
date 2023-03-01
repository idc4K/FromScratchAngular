from django.shortcuts import render
from .serializers import *
from .data import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,status,views,permissions,viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,UpdateAPIView
from django.utils import timezone

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

@api_view(['PATCH'])
@csrf_exempt
# @permission_classes([IsAuthenticated,autorisation])	
def updateMovie(request,pk):
    serializer_class = Datas
    donnee = Data.objects.get(id=pk)
    donnee.updated_at = timezone.now()
    serializer = serializer_class(donnee, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteMovie(request, pk):
    serializers = Datas
    donnee = Data.objects.get(id=pk)
    donnee.deleted_at = timezone.now()
    
    donnee.delete()
    return Response('Data deleted')

        
    
    
# Create your views here.
