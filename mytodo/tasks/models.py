from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    # attachs