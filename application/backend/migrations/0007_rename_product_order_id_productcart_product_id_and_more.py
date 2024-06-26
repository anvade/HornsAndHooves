# Generated by Django 5.0.4 on 2024-04-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_order_product_id_order_product_order_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcart',
            old_name='product_order_id',
            new_name='product_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='product_order_id',
            field=models.ManyToManyField(blank=True, to='backend.productcart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_order_id',
            field=models.ManyToManyField(blank=True, to='backend.productorder'),
        ),
    ]
