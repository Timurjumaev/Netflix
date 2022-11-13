from rest_framework.exceptions import ValidationError
from .models import *
from rest_framework.serializers import ModelSerializer

class AktyorSerializer(ModelSerializer):
    class Meta:
        model=Aktyor
        fields='__all__'

    def validate_jins(self, qiymat):
        if qiymat.lower()!='erkak' and qiymat.lower()!='ayol':
            raise ValidationError("Jins kiritishda hatoga yol qoydingiz!")
        return qiymat

class KinoSerializer(ModelSerializer):
    aktyorlar=AktyorSerializer(many=True)
    class Meta:
        model=Kino
        fields='__all__'

class CommentSerializer(ModelSerializer):
    kino=KinoSerializer()
    class Meta:
        model=Comment
        fields='__all__'