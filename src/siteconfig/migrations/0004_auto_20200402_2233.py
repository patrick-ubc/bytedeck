# Generated by Django 2.2.9 on 2020-04-03 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteconfig', '0003_auto_20200402_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteconfig',
            old_name='hackerspace_ai',
            new_name='deck_ai',
        ),
    ]
