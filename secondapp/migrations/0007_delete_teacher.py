# Generated by Django 4.2 on 2023-05-18 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0006_alter_register_table_contact_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]