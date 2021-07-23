from django.db.models import fields
from rest_framework import serializers
from .models import teammodels

class serializationclass(serializers.ModelSerializer):
    class Meta:
        model= teammodels
        fields="__all__"