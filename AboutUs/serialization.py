from django.db.models import fields
from rest_framework import serializers
from .models import AboutModels

class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model= AboutModels
        fields="__all__"

