# Generated by Django 3.2.20 on 2024-08-04 13:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0109_alter_creature_passive_perception'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='challenge_rating_decimal',
            field=models.DecimalField(decimal_places=3, default=0, help_text='Challenge Rating field as a decimal number.', max_digits=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creature',
            name='experience_points_integer',
            field=models.IntegerField(help_text='Optional override for calculated XP based on CR.', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]