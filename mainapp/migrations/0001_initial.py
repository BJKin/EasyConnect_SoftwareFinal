# Generated by Django 5.2.2 on 2025-06-09 14:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=100, unique=True)),
                ('assigned_ticket', models.CharField(blank=True, max_length=100, null=True)),
                ('available', models.BooleanField(default=True)),
                ('last_seen', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=255)),
                ('attendee_code', models.CharField(max_length=10, unique=True)),
                ('employee_code', models.CharField(max_length=10, unique=True)),
                ('vendor_code', models.CharField(max_length=10, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosted_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('joined_events', models.ManyToManyField(related_name='employees', to='mainapp.event')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(max_length=100, unique=True)),
                ('event_name', models.CharField(max_length=200)),
                ('event_date', models.DateTimeField()),
                ('ticket_type', models.CharField(choices=[('GA', 'General Admission'), ('VIP', 'VIP')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.event')),
                ('ticket_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiated_connections', to='mainapp.ticket')),
                ('ticket_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_connections', to='mainapp.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('attendee', 'Attendee'), ('vendor', 'Vendor'), ('admin', 'Admin'), ('employee', 'Employee')], max_length=10)),
                ('bio', models.TextField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('goal', models.TextField(blank=True)),
                ('reps', models.TextField(blank=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
