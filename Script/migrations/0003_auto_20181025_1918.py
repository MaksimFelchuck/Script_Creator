# Generated by Django 2.1.2 on 2018-10-25 12:18

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Script', '0002_auto_20181025_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='creator',
            field=models.ForeignKey(blank=True, default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
