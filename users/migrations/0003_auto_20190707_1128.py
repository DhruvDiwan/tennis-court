# Generated by Django 2.2 on 2019-07-07 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='FirstName',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Surname',
            field=models.CharField(max_length=300, null=True),
        ),
    ]