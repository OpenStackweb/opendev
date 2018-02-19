from django.db import models, migrations
from django.contrib.auth.models import Group, Permission


def apply_migration(apps, schema_editor):
    editor = Group.objects.create(name='Editor')
    
    apps = ['content', 'menus']
    permissions = Permission.objects.filter(content_type__app_label__in=apps)
    for perm in permissions:
        editor.permissions.add(perm)


def revert_migration(apps, schema_editor):
    Group.objects.filter(
        name__in=[
            u'Editor',
        ]
    ).delete()


class Migration(migrations.Migration):
    
    dependencies = [
        ('content', '0076_auto_20180215_1455'),
    ]
    operations = [
        migrations.RunPython(apply_migration, revert_migration)
    ]

