# Generated by Django 4.0.4 on 2022-05-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuingorder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuingorder',
            name='iodate',
            field=models.DateField(auto_now=True),
        ),
    ]
