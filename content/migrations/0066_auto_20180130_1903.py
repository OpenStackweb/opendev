# Generated by Django 2.0.1 on 2018-01-30 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0065_auto_20180130_1839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='talk',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
    ]