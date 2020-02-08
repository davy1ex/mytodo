from django.db import models


class Task(models.Model):
    type_task = models.CharField(max_length=64, default="inbox")
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    # attachs