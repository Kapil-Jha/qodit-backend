from django.db.models import fields
from rest_framework import serializers
from .models import ChooseLeftModels


class SerializationChoose(serializers.ModelSerializer):
    class Meta:
        model=ChooseLeftModels
        fields="__all__"