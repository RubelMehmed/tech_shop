# Generated by Django 4.0.5 on 2023-02-06 15:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('delevery_address', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=15)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itshop.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itshop.product')),
            ],
        ),
    ]