# Generated by Django 3.0.6 on 2020-05-23 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_auto_20200523_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='context',
            new_name='content',
        ),
    ]
