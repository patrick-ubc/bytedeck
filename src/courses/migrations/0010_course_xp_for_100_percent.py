# Generated by Django 2.2.9 on 2020-03-09 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20200104_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='xp_for_100_percent',
            field=models.PositiveIntegerField(default=1000),
        ),
    ]
