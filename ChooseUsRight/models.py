from django.db import models



class ChooseRightModels(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField( max_length=100)