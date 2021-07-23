from django.http.response import JsonResponse
from rest_framework import status
from .serialization import SerializationClass, SerializationClass
from .models import ServiceModels, ServiceModels
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

@api_view(['GET','POST','DELETE'])
def qoditserv(request):
    if request.method=='GET':
        results=ServiceModels.objects.all()
        Serialize=SerializationClass(results,many=True)
        return Response(Serialize.data)
    elif request.method=='POST' :
        jason_data = JSONParser().parse(request)
        serializer = SerializationClass(data = jason_data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        results=ServiceModels.objects.all()
        results.delete()
        return Response("Deleted")




@api_view(['DELETE','PUT','GET'])
def delqoditserv(request,pk):
    if request.method=='DELETE':
        event= ServiceModels.objects.get(id=pk) 
        event.delete()
        return Response("Deleted")
    elif request.method=='PUT':
        results=ServiceModels.objects.get(id=pk)
        data=request.data
        results.title=data["title"]
        results.body=data["body"]
        results.image=data["image"]
        results.alt=data["alt"]
        results.save() 
        serializer=SerializationClass(results)
        return Response('Updated',serializer.data)
    else:
        results=ServiceModels.objects.get(id=pk)
        Serialize=SerializationClass(results)
        return JsonResponse(Serialize.data)


