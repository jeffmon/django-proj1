from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField(default='')
    image = models.ImageField(upload_to='images/')

    def summary(self):  # makes a summary function to shorten body to 100 characters
        return self.body[:100]
