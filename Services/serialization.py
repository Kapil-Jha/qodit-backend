from django.db.models import fields
from rest_framework import serializers
from .models import ServiceModels

class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model= ServiceModels
        fields="__all__"