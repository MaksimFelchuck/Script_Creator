# Generated by Django 2.1.2 on 2018-10-28 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Script', '0004_auto_20181025_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='create_date',
            field=models.DateField(default='2018-10-28'),
        ),
        migrations.AlterField(
            model_name='script',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
