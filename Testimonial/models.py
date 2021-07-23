from django.db import models

class TestiModels(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField( max_length=100)
    subtitle=models.CharField(max_length=100,default='')
    body=models.CharField(max_length=1000,default="")
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    alt=models.CharField(max_length=50, default='some string')