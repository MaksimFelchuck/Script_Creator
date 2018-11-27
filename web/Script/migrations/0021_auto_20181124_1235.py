# Generated by Django 2.0.5 on 2018-11-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Script', '0020_auto_20181115_2115'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Script_from_github',
        ),
        migrations.AddField(
            model_name='script',
            name='parameter_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='script',
            name='create_date',
            field=models.DateField(default='2018-11-24'),
        ),
    ]