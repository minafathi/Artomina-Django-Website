from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    more = models.TextField()
    pic = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.title



