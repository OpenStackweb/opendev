# Generated by Django 2.0.1 on 2018-02-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_base_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='custom_css',
            field=models.TextField(blank=True, null=True),
        ),
    ]
