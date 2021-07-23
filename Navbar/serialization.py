from rest_framework import serializers
from .models import NavModels

class SerializationNav(serializers.ModelSerializer):
    class Meta:
        model=NavModels
        fields="__all__"

