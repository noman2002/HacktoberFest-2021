# Generated by Django 3.0.7 on 2020-06-25 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cart',
            new_name='cartItem',
        ),
    ]