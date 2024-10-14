# Generated by Django 4.2.7 on 2024-09-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_transaction_discount_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='amount_paid',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sale',
            name='remaining_balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sale',
            name='total_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]