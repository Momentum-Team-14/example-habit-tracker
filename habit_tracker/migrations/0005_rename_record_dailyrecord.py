# Generated by Django 4.0.3 on 2022-03-26 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0004_record_unique_for_habit_and_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Record',
            new_name='DailyRecord',
        ),
    ]
