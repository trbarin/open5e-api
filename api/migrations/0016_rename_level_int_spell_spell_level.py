# Generated by Django 3.2.18 on 2023-04-14 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20230414_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spell',
            old_name='level_int',
            new_name='spell_level',
        ),
    ]