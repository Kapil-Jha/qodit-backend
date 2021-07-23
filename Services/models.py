from django.db import models



class ServiceModels(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField( max_length=100)
    body=models.CharField(max_length=1000)
    # image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='null')
    alt=models.CharField(max_length=50, default='some string')