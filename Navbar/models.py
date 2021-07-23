from django.db import models


class NavModels(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField( max_length=100)
    
