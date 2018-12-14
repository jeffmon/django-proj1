from django.db import models


class Job(models.Model):
    # upload_to specified name or directory
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
