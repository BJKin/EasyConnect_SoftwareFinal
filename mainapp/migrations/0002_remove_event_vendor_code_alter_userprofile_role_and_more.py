# Generated by Django 5.2.2 on 2025-06-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='vendor_code',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('attendee', 'Attendee'), ('admin', 'Admin'), ('employee', 'Employee')], max_length=10),
        ),
        migrations.DeleteModel(
            name='VendorInfo',
        ),
    ]
