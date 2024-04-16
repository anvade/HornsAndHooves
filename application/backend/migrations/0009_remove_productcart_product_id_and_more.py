# Generated by Django 5.0.4 on 2024-04-14 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_rename_product_order_id_cart_product_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcart',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='product_id',
        ),
        migrations.AddField(
            model_name='productcart',
            name='product_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='backend.product'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='product_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='backend.product'),
        ),
    ]