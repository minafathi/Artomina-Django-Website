from django.db import models

class Cat(models.Model):
    title = models.CharField(max_length=225)
    pic = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.title

class Paint(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    size = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    order = models.IntegerField(default=0)
    cat = models.ForeignKey('Cat', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img', default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order',]