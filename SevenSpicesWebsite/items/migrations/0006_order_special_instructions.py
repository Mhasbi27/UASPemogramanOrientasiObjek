# Generated by Django 2.1.2 on 2018-12-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='special_instructions',
            field=models.TextField(blank=True, max_length=256),
        ),
    ]