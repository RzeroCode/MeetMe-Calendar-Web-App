# Generated by Django 3.0.4 on 2020-06-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventCalendar', '0019_auto_20200506_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingparticipation',
            name='meetingEventID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
