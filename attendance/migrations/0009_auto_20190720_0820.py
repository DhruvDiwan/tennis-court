# Generated by Django 2.2 on 2019-07-20 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_auto_20190720_0817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendanceevent',
            old_name='status',
            new_name='event_status',
        ),
    ]
