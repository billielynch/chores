# Generated by Django 5.0.3 on 2024-03-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_alter_task_completed_last"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="completed_last",
            field=models.DateField(blank=True, null=True),
        ),
    ]