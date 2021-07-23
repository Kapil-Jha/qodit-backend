from django.http.response import JsonResponse
from rest_framework import  status
from .serialization import SerializationChoose
from .models import ChooseLeftModels
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser




@api_view(['DELETE','PUT','GET'])
def delchooseus(request,pk):
    if request.method=='DELETE':
        event= ChooseLeftModels.objects.get(id=pk) 
        event.delete()
        return Response("deleted")
    elif request.method=='PUT':
         results=ChooseLeftModels.objects.get(id=pk)
         data=request.data
         results.title=data["title"]
         results.save() 
         serializer=SerializationChoose(results)
         return Response(serializer.data)
    else:
        results=ChooseLeftModels.objects.get(id=pk)
        Serialize=SerializationChoose(results)
        return JsonResponse(Serialize.data)
  



@api_view(['GET','POST','DELETE'])
def chooseus(request):
    if request.method=='GET':
        results=ChooseLeftModels.objects.all()
        Serialize=SerializationChoose(results,many=True)
        return Response(Serialize.data)
    elif request.method=='POST':
        jason_data = JSONParser().parse(request)
        serializer = SerializationChoose(data = jason_data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        results=ChooseLeftModels.objects.all()
        results.delete()
        return Response("Deleted")


   
    
