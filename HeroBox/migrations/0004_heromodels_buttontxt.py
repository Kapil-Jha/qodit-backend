# Generated by Django 3.2.5 on 2021-07-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeroBox', '0003_auto_20210719_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='heromodels',
            name='buttontxt',
            field=models.CharField(default='', max_length=50),
        ),
    ]