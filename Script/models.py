import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class script(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    script_name = models.CharField(max_length=40, unique=True, db_index=True, primary_key=True)
    script = models.TextField()
    create_date = models.DateField(default=str(datetime.datetime.now())[:10])

    def __str__(self):
        return self.script_name
