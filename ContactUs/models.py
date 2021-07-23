from django.db import models


class Contact(models.Model):
   
    name=models.CharField(max_length=50,default='name')
    email = models.EmailField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.email