# Generated by Django 5.0.4 on 2024-04-14 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_remove_productcart_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcart',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.product'),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.product'),
        ),
    ]
