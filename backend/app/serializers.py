from .data import *
from rest_framework import serializers


class Datas(serializers.ModelSerializer):
    
    class Meta:
        model = Data
        fields = ['id','name','desc','image','genre_movie']

class Genres(serializers.ModelSerializer):
    
    class Meta:
        model = genre
        fields = ['id','name_genre']