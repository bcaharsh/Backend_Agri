# Generated by Django 5.0.1 on 2024-03-16 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizer_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Price', models.IntegerField(default=0)),
                ('Product_image', models.ImageField(default=None, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='croppreservation',
            name='Crop_image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
