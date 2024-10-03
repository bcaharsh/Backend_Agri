# Generated by Django 5.0.1 on 2024-03-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNumber', models.CharField(max_length=20)),
                ('DateOfBooking', models.DateField()),
                ('TimeSlot', models.TimeField()),
            ],
        ),
    ]