# Generated by Django 2.2.12 on 2020-05-09 05:11

from django.db import migrations


# Can't use fixtures because load_fixtures method is janky with django-tenant-schemas
def load_initial_data(apps, schema_editor):
    BadgeType = apps.get_model('badges', 'BadgeType')

    # add some initial data if none has been created yet
    if not BadgeType.objects.exists():
        BadgeType.objects.create(
            name="Talent",
            sort_order=1,
            description="Talents are badges that are automatically granted by completing a specific set of prerequisites.",
            repeatable=True,
            fa_icon="fa-hand-spock-o"
        )
        BadgeType.objects.create(
            name="Award",
            sort_order=3,
            description="Awards are badges that are manually granted by teachers.",
            repeatable=True,
            fa_icon="fa-diamond"
        )


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0003_auto_20190809_1136'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]