# Generated by Django 3.1.8 on 2021-05-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='posted',
            field=models.DateTimeField(null=True),
        ),
    ]