# Generated by Django 2.0.1 on 2018-01-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20180111_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
    ]