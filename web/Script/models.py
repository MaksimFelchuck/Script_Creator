import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class script(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    script_name = models.CharField(max_length=40, unique=True, db_index=True, primary_key=True)
    script = models.TextField()
    create_date = models.DateField(default=str(datetime.datetime.now())[:10])
    script_format = models.CharField(max_length=20, default=None)
    parameter_name = models.CharField(max_length=20, default='')
    parameter = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.script_name


class History(models.Model):
    host_script = models.ForeignKey(script, on_delete=models.CASCADE, default=None)
    run_time = models.CharField(max_length=50)
    active_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    console_output = models.TextField(default=None)
    status = models.TextField(default='')

    def __str__(self):
        return str(self.host_script)

