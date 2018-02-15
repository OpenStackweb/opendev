# Generated by Django 2.0.1 on 2018-02-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0073_auto_20180209_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='style',
            options={'ordering': ('title',)},
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='email',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='image',
        ),
        migrations.AlterField(
            model_name='block',
            name='content_justify',
            field=models.CharField(choices=[('LEFT', '⯇ Left'), ('CENTER', '￭ Center'), ('RIGHT', '⯈ Right')], default='LEFT', max_length=6, verbose_name='Content align'),
        ),
        migrations.AlterField(
            model_name='block',
            name='layout',
            field=models.CharField(choices=[('ONECOL', '□ One column'), ('TWOCOL', '◫ Two columns')], default='ONECOL', max_length=6),
        ),
        migrations.AlterField(
            model_name='module',
            name='content_width',
            field=models.CharField(choices=[('WIDE', '█ Wide'), ('SEMIWIDE', '▌ Semi wide'), ('NARROW', '▎ Narrow')], default='WIDE', max_length=8),
        ),
        migrations.AlterField(
            model_name='module',
            name='image_position',
            field=models.CharField(choices=[('LEFT', '◧ Left'), ('RIGHT', '◨ Right')], default='LEFT', max_length=6),
        ),
    ]