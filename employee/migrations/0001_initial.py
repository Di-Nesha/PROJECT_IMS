# Generated by Django 4.0.3 on 2022-03-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CiviStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('fullname', models.CharField(max_length=200)),
                ('callingname', models.CharField(max_length=75)),
                ('png', models.ImageField(upload_to='', verbose_name='jpeg')),
                ('nic', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('land', models.IntegerField()),
                ('regdate', models.DateField(auto_now=True)),
                ('gender_id', models.CharField(max_length=15)),
                ('civilstatus_id', models.CharField(max_length=15)),
                ('employeestatus_id', models.CharField(max_length=15)),
                ('designation_id', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]