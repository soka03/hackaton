# Generated by Django 5.0.7 on 2024-08-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_order_pickup_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='progress',
            field=models.TextField(default='waiting'),
        ),
    ]
