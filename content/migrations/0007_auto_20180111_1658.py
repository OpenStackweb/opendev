# Generated by Django 2.0.1 on 2018-01-11 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20180111_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modules', to='content.Page'),
        ),
    ]