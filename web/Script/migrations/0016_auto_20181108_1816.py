# Generated by Django 2.1.2 on 2018-11-08 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Script', '0015_auto_20181105_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='active_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='history',
            name='code',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='history',
            name='run_time',
            field=models.DateTimeField(default='2018-11-08 18:16:29.084350'),
        ),
        migrations.AlterField(
            model_name='script',
            name='create_date',
            field=models.DateField(default='2018-11-08'),
        ),
    ]
