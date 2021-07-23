from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.serializers import Serializer
from .serialization import SerializationNav
from .models import NavModels
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser



@api_view(['DELETE','PUT','GET'])
def qodit(request,pk):
    if request.method=='DELETE':
        event= NavModels.objects.get(id=pk) 
        event.delete()
        return Response("Deleted")
    elif request.method=='PUT':
        results=NavModels.objects.get(id=pk)
        data=request.data
        results.title=data["title"]
        results.save() 
        serializer=SerializationNav(results)
        return Response('Updated',serializer.data)
    else:
        results=NavModels.objects.get(id=pk)
        Serialize=SerializationNav(results)
        return JsonResponse(Serialize.data)
  

@api_view(['GET','POST','DELETE'])
def showqodit(request):
    if request.method=='GET':
        results=NavModels.objects.all()
        Serialize=SerializationNav(results,many=True)
        return Response(Serialize.data)
    elif request.method=='POST':
        jason_data = JSONParser().parse(request)
        serializer = SerializationNav(data = jason_data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        results=NavModels.objects.all()
        results.delete()
        return Response("Deleted")

