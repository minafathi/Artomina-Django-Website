from django.db import models

class Me(models.Model):
    name = models.CharField(max_length=225)
    pic = models.ImageField(upload_to='static/img')
    description = models.TextField()
