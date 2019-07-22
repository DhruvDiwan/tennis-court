# Generated by Django 2.2 on 2019-07-22 05:53

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0010_auto_20190720_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendanceperson',
            name='intercom',
        ),
        migrations.AddField(
            model_name='attendanceperson',
            name='subtitle',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='attendanceperson',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='attendanceperson',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=300, null=True, region=None),
        ),
    ]
