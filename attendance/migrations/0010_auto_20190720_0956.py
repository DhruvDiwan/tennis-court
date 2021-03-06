# Generated by Django 2.2 on 2019-07-20 04:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0009_auto_20190720_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='coaches',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='batch',
            name='subtitle',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
