# Generated by Django 2.1.2 on 2018-11-01 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Script', '0006_auto_20181028_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='create_date',
            field=models.DateField(default='2018-11-01'),
        ),
        migrations.AlterField(
            model_name='script',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
