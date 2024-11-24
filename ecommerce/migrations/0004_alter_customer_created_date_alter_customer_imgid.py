# Generated by Django 4.1 on 2024-11-17 10:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_customer_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 17, 10, 31, 11, 992485)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='imgid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.images'),
        ),
    ]