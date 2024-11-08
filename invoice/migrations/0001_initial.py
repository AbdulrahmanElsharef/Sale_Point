# Generated by Django 4.2.7 on 2024-11-04 10:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='barcode')),
                ('des', models.CharField(max_length=128, verbose_name='Description')),
                ('item_type', models.BooleanField(choices=[(True, 'Item'), (False, 'Service')], default=True, verbose_name='Type')),
                ('quantity', models.PositiveIntegerField(default=0, help_text='Set to 0 if Items')),
                ('price', models.PositiveIntegerField(default=0)),
                ('discount', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
            ],
            options={
                'verbose_name_plural': 'Items ',
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('balance_amount', models.IntegerField(default=0, verbose_name='Balance Amount')),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=128)),
                ('reg_no', models.CharField(max_length=50, verbose_name='Registration Number')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_date', models.DateField(default=datetime.date.today, verbose_name='Bill Date')),
                ('total_amount', models.PositiveIntegerField(default=0)),
                ('amount_paid', models.PositiveIntegerField(default=0)),
                ('remaining_balance', models.PositiveIntegerField(default=0)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='invoice.party', verbose_name='Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('quantity', models.IntegerField(default=0, help_text='Set to 0 if Items')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('discount_percent', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='invoice.itemservice')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='invoice.sale')),
            ],
        ),
        migrations.CreateModel(
            name='PartyBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField(default=datetime.date.today, verbose_name='Payment Date')),
                ('amount', models.IntegerField(default=0)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='balances', to='invoice.party', verbose_name='Customer')),
            ],
        ),
    ]
