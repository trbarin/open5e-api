# Generated by Django 3.2.20 on 2024-09-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0118_creatureaction_form_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='subcategory',
            field=models.CharField(help_text='What subcategory this creature belongs to.', max_length=100, null=True),
        ),
    ]
