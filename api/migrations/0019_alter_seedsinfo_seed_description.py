# Generated by Django 5.0.1 on 2024-03-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_rename_titel_govermentschem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seedsinfo',
            name='Seed_Description',
            field=models.TextField(max_length=300),
        ),
    ]