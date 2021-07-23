from django.db.models import fields
from rest_framework import serializers
from .models import TestiModels

class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model= TestiModels
        fields="__all__"