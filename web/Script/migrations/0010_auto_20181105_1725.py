# Generated by Django 2.1.2 on 2018-11-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Script', '0009_auto_20181102_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='run_time',
            field=models.DateField(default='2018-11-05'),
        ),
        migrations.AlterField(
            model_name='script',
            name='create_date',
            field=models.DateField(default='2018-11-05'),
        ),
    ]
