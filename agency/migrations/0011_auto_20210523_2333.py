# Generated by Django 3.2 on 2021-05-23 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0010_auto_20210523_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixed_booking',
            name='allocated_hotel',
        ),
        migrations.CreateModel(
            name='FIXED_TRIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('ISLAMABAD', 'ISLAMABAD'), ('RAWALPINDI', 'RAWALPINDI')], max_length=100)),
                ('destination', models.CharField(choices=[('MURREE', 'MURREE'), ('NATHIA GALI', 'NATHIA GALI'), ('NARAN KAGHAN', 'NARAN KAGHAN'), ('KASHMIR', 'KASHMIR'), ('SAWAT', 'SAWAT')], max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('available_seats', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveBigIntegerField(default=0)),
                ('allocated_hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='agency.hotel')),
            ],
            options={
                'verbose_name': 'Fixed Trip',
            },
        ),
    ]
