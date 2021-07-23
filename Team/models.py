from django.db import models

class teammodels(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField( max_length=100)
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Alt=models.CharField(max_length=50, default='some string')
    title2=models.CharField( max_length=100)
