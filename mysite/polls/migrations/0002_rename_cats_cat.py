# Generated by Django 4.0.3 on 2022-03-03 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cats',
            new_name='Cat',
        ),
    ]
