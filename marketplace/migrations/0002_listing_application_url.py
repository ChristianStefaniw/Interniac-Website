# Generated by Django 3.1.6 on 2021-02-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='application_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
