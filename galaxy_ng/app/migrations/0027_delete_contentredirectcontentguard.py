# Generated by Django 3.2.12 on 2022-03-23 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0026_migrate_to_core_content_guard'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContentRedirectContentGuard',
        ),
    ]