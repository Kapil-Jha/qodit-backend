from django.db.models import fields
from rest_framework import serializers
from .models import HeroModels

class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model= HeroModels
        fields="__all__"