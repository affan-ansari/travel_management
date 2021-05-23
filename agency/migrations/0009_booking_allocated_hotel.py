# Generated by Django 3.2 on 2021-05-22 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0008_booking_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='allocated_hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='agency.hotel'),
        ),
    ]
