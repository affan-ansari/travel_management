# Generated by Django 3.2 on 2021-05-22 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agency', '0007_alter_hotel_fare_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
    ]
