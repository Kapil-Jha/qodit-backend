# Generated by Django 3.2.5 on 2021-07-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Testimonial', '0002_testimodels_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimodels',
            name='body',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
