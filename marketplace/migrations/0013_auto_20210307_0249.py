# Generated by Django 3.1.6 on 2021-03-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210307_0225'),
        ('marketplace', '0012_auto_20210307_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='acceptances',
            field=models.ManyToManyField(blank=True, related_name='listing_acceptances', to='accounts.StudentProfile'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='applications',
            field=models.ManyToManyField(blank=True, related_name='applications', to='accounts.StudentProfile'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='interview_requests',
            field=models.ManyToManyField(blank=True, related_name='interviews', to='accounts.StudentProfile'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rejections',
            field=models.ManyToManyField(blank=True, related_name='listing_rejections', to='accounts.StudentProfile'),
        ),
    ]