# Generated by Django 4.2.7 on 2024-09-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_alter_itemservice_options_itemservice_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='discount_percent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]