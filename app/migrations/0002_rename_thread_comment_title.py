# Generated by Django 4.0.6 on 2022-07-16 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='thread',
            new_name='title',
        ),
    ]
