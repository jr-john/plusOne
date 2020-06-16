# Generated by Django 3.0.6 on 2020-06-16 21:22

import action.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[['airport', 'Rajiv Gandhi International Airport'], ['railway-secunderabad', 'Secunderabad Railway Station'], ['railway-lingam', 'Lingampally Railway Station'], ['railway-begumpet', 'Begumpet Railway Station'], ['railway-nampally', 'Hyderabad Deccan Railway Station (Nampally)'], ['bus-mg', 'Mahatma Gandhi Bus Station'], ['college', 'IIIT Hyderabad Campus']], default='college', max_length=100)),
                ('destination', models.CharField(choices=[['airport', 'Rajiv Gandhi International Airport'], ['railway-secunderabad', 'Secunderabad Railway Station'], ['railway-lingam', 'Lingampally Railway Station'], ['railway-begumpet', 'Begumpet Railway Station'], ['railway-nampally', 'Hyderabad Deccan Railway Station (Nampally)'], ['bus-mg', 'Mahatma Gandhi Bus Station'], ['college', 'IIIT Hyderabad Campus']], default='airport', max_length=100)),
                ('journey_date', models.DateField(default=django.utils.timezone.now)),
                ('journey_time', models.TimeField(default=action.models.def_journey_time)),
                ('is_active', models.BooleanField(default=False)),
                ('owner', models.CharField(blank=True, max_length=100, null=True)),
                ('minima', models.IntegerField(default=30)),
                ('maxima', models.IntegerField(default=20)),
            ],
        ),
    ]
