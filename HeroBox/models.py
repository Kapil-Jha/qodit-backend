from django.db import models

class HeroModels(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField( max_length=100)
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    body=models.CharField( max_length=500,default="")
    alt=models.CharField(max_length=50, default='')
    buttontxt=models.CharField( max_length=50,default='')
