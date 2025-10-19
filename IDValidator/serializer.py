from rest_framework import serializers
from .utils import validate_id

class IDCardSerializer(serializers.Serializer):
    national_id = serializers.CharField(required = True , max_length=14 , min_length=14)


    def validate_national_id(self,value):
        if not value.isdigit():
            raise serializers.ValidationError("National ID must contain only digits.")
    
        id = validate_id(value)
        if not id["valid"]:
            raise serializers.ValidationError(id["reason"])
        
        self.parsed_data = id
        return id
    
class IDOutputSerializer(serializers.Serializer):
    birth_date = serializers.DateField(format="%Y-%m-%d")
    province = serializers.CharField()
    gender = serializers.CharField()
    births_same_day = serializers.IntegerField()