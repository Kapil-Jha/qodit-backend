# Generated by Django 3.2.5 on 2021-07-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammodels',
            name='Alt',
            field=models.CharField(default='some string', max_length=50),
        ),
    ]
