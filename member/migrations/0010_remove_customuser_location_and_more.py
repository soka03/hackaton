# Generated by Django 5.0.7 on 2024-07-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_customuser_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='location',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='detail_location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='dong',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='district',
            field=models.CharField(default='', max_length=100),
        ),
    ]
