# Generated by Django 5.0 on 2024-02-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0002_alter_donar_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donar',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=20),
        ),
    ]