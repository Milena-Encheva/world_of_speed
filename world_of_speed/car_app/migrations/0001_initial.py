# Generated by Django 4.2.11 on 2024-04-16 07:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import world_of_speed.car_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Rally', 'Rally'), ('Open-wheel', 'Open-wheel'), ('Kart', 'Kart'), ('Drag', 'Drag'), ('Other', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(1), world_of_speed.car_app.validators.validate_year])),
                ('image_url', models.URLField(error_messages={'unique': 'This image URL is already in use! Provide a new one.'}, unique=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.profile')),
            ],
        ),
    ]