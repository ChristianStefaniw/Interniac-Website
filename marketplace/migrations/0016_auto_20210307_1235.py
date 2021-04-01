# Generated by Django 3.1.6 on 2021-03-07 17:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketplace', '0015_auto_20210307_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='employer_acceptances',
            field=models.ManyToManyField(blank=True, related_name='employer_acceptances', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='employer_interview_requests',
            field=models.ManyToManyField(blank=True, related_name='employer_interview_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='employer_rejections',
            field=models.ManyToManyField(blank=True, related_name='employer_rejections', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='student_acceptances',
            field=models.ManyToManyField(blank=True, related_name='student_acceptances', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='student_interview_requests',
            field=models.ManyToManyField(blank=True, related_name='student_interview_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='student_rejections',
            field=models.ManyToManyField(blank=True, related_name='student_rejections', to=settings.AUTH_USER_MODEL),
        ),
    ]
