from .data import Data
from rest_framework import serializers


class Datas(serializers.ModelSerializer):
    
    class Meta:
        model = Data
        fields = ['id','name','desc','image']