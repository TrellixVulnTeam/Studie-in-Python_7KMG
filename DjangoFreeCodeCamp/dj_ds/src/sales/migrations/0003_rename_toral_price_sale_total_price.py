# Generated by Django 3.2.4 on 2021-06-28 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sale_toral_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='toral_price',
            new_name='total_price',
        ),
    ]
