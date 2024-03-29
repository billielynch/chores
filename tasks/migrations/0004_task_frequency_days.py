# Generated by Django 5.0.3 on 2024-03-14 07:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_alter_task_completed_last"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="frequency_days",
            field=models.PositiveIntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(1)]
            ),
            preserve_default=False,
        ),
    ]
