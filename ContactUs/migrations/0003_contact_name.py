# Generated by Django 3.2.5 on 2021-07-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactUs', '0002_auto_20210715_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Name',
            field=models.TextField(default='name', max_length=50),
        ),
    ]
