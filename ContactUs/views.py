from django.conf import settings
from django.http.response import JsonResponse
from rest_framework import status
from .serialization import SerializationClass
from .models import Contact
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.core.mail import send_mail




    

@api_view(['DELETE'])        
def deleteall(request):
    if request.method=='DELETE':
        results=Contact.objects.all()
        results.delete()
        return Response("Deleted")
        

@api_view(['DELETE'])
def deletelist(request,pk):
    if request.method=='DELETE':
        event= Contact.objects.get(id=pk) 
        event.delete()
        return Response("Deleted")


        
@api_view(['POST','GET'])
def contactsendmail(request):
     if request.method=='POST':
         jason_data = JSONParser().parse(request)
         msg = jason_data['name']+"\n"+jason_data['message']+"\n"+jason_data['email']
         send_mail(
         'Website Enquiry',
          msg,
          jason_data['email'] ,
          [settings.EMAIL_HOST_USER ]
        )
         serializer = SerializationClass(data = jason_data)
         if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     else:
        results=Contact.objects.all()
        Serialize=SerializationClass(results,many=True)
        return Response(Serialize.data)
     



 