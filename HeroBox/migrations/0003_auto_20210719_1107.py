# Generated by Django 3.2.5 on 2021-07-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeroBox', '0002_heromodels_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='heromodels',
            name='body',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='heromodels',
            name='Alt',
            field=models.CharField(default='', max_length=50),
        ),
    ]
