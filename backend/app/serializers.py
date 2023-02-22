from .data import *
from rest_framework import serializers

class GenreData(serializers.ModelSerializer):
    
    class Meta:
        model = genre
        fields = ['id','name_genre']
    
class Datas(serializers.ModelSerializer):
    
    class Meta:
        model = Data
        fields = ['id','name','desc','image','genre_movie']

class DatasView(serializers.ModelSerializer):
    genre_movie = GenreData(read_only=True)
    class Meta:
        model = Data
        fields = ['id','name','desc','image','genre_movie']
        
class Genres(serializers.ModelSerializer):
    
    class Meta:
        model = genre
        fields = ['id','name_genre']