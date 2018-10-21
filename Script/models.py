import datetime

from django.db import models


# Create your models here.
class creators(models.Model):
    creator_name = models.CharField(max_length=40, unique=True, db_index=True, primary_key=True)
    creator_email = models.EmailField()
    creator_password = models.CharField(max_length=40, unique=True, db_index=True)

    def __str__(self):
        return self.creator_name


class script(models.Model):
    creator = models.ForeignKey(creators, on_delete=models.CASCADE)
    script_name = models.CharField(max_length=40, unique=True, db_index=True, primary_key=True)
    script = models.TextField()
    create_date = models.DateField(default=str(datetime.datetime.now())[:10])

    def __str__(self):
        return self.script_name
