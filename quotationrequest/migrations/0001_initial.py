# Generated by Django 4.0.4 on 2022-05-13 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='QuotationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('regdate', models.DateField(auto_now=True)),
                ('duedate', models.DateField()),
                ('notes', models.TextField()),
                ('employee', models.ForeignKey(db_column='employee_id', on_delete=django.db.models.deletion.CASCADE, to='employee.new')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotationrequest.status')),
                ('supplier', models.ForeignKey(db_column='supplier_id', on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier')),
            ],
        ),
    ]