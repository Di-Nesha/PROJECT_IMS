# Generated by Django 4.0.4 on 2022-04-15 18:26

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_bank_alter_supplier_bankname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='creditlimit_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', '$'), ('LKR', 'Rs')], default='XYZ', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='tobepaid_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', '$'), ('LKR', 'Rs')], default='XYZ', editable=False, max_length=3),
        ),
    ]
