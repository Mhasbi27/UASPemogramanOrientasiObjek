# Generated by Django 2.1.2 on 2018-12-03 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_auto_20181203_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]