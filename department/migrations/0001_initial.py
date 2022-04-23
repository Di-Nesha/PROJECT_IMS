# Generated by Django 4.0.4 on 2022-04-23 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
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
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('land', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('fax', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('notes', models.TextField()),
                ('regdate', models.DateField(auto_now=True)),
                ('employee', models.ForeignKey(db_column='employee_id', on_delete=django.db.models.deletion.CASCADE, to='employee.new')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.status')),
            ],
        ),
    ]
