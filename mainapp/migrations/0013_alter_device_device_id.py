# Generated by Django 5.2.1 on 2025-06-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0012_ticket_event_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="device",
            name="device_id",
            field=models.CharField(max_length=100),
        ),
    ]
