# Generated by Django 3.1.7 on 2021-03-18 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210318_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme',
            old_name='author',
            new_name='body',
        ),
    ]
