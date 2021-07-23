
from rest_framework import serializers
from .models import FeaturesModels

class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model= FeaturesModels
        fields="__all__"