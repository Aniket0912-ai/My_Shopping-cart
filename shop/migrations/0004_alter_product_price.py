# Generated by Django 3.2 on 2021-07-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
