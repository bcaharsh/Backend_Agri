# Generated by Django 5.0.1 on 2024-03-13 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CropPreservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Crop_name', models.CharField(max_length=200)),
                ('Crop_Temp', models.FloatField(blank=True, null=True)),
                ('Crop_Description', models.TextField()),
            ],
        ),
    ]
