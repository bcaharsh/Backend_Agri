# Generated by Django 5.0.1 on 2024-03-17 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addtocart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user_registration')),
                ('Product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fertilizer_product')),
            ],
        ),
    ]
