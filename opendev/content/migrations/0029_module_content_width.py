# Generated by Django 2.0.1 on 2018-01-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0028_auto_20180116_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='content_width',
            field=models.CharField(choices=[('BLOCK', 'Block'), ('SPONSOR', 'Sponsorship'), ('IMAGEGALLERY', 'Image gallery')], default='WIDE', max_length=6),
        ),
    ]
