# Generated by Django 2.0.5 on 2018-11-27 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Script', '0021_auto_20181124_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='patameter',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='script',
            name='create_date',
            field=models.DateField(default='2018-11-27'),
        ),
    ]