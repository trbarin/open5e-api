# Generated by Django 3.2.20 on 2024-09-24 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0118_creatureaction_form_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='casting_time',
            field=models.TextField(choices=[('reaction', 'Reaction'), ('bonus-action', '1 Bonus Action'), ('action', '1 Action'), ('1minute', '1 Minute'), ('5minutes', '5 Minutes'), ('10minutes', '10 Minutes'), ('1hour', '1 Hour'), ('4hours', '4 Hours'), ('7hours', '7 Hours'), ('8hours', '8 Hours'), ('9hours', '9 Hours'), ('12hours', '12 Hours'), ('24hours', '24 Hours'), ('1week', '1 Week')], help_text="Casting time key, such as 'action'"),
        ),
    ]
