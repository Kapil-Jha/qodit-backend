from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import (get_object_or_404,render, HttpResponseRedirect)
from rest_framework import response, status
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .serialization import serializationclass
from .models import teammodels
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

@api_view(['GET','POST'])
def qoditteam(request):
    if request.method=='GET':
        results=teammodels.objects.all()
        Serialize=serializationclass(results,many=True)
        return Response(Serialize.data)
    else:
        jason_data = JSONParser().parse(request)
        serializer = serializationclass(data = jason_data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE','PUT'])
def delqoditteam(request,pk):
    if request.method=='DELETE':
        event= teammodels.objects.get(id=pk) 
        event.delete()
        return Response("deleted")
    else:
        results=teammodels.objects.get(id=pk)
        data=request.data
        results.title=data["title"]
        results.body=data["body"]
        results.image=data["image"]
        results.title2=data["title2"]
        results.save() 
        serializer=serializationclass(results)
        return Response(serializer.data)




