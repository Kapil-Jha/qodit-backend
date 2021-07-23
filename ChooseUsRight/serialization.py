from django.db.models import fields
from rest_framework import serializers
from .models import ChooseRightModels


class SerializationClass(serializers.ModelSerializer):
    class Meta:
        model=ChooseRightModels
        fields="__all__"