# Generated by Django 3.2.1 on 2021-05-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GolfStatsApp', '0002_round_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='date',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
