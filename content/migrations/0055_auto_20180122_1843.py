# Generated by Django 2.0.1 on 2018-01-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0054_auto_20180122_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='type',
            field=models.CharField(choices=[('BLOCK', 'Block'), ('SPONSORSHIP', 'Sponsorship'), ('IMAGEGALLERY', 'Image gallery'), ('VIDEOGALLERY', 'Video gallery')], max_length=12, null=True),
        ),
    ]
