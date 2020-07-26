from django.db import models
from django.core.validators import RegexValidator


class Kind(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title

class Order(models.Model):
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='static/img/order')
    phone = models.CharField(validators=[RegexValidator(regex='^\+[0-9]{12}$')], max_length=13)
    email = models.EmailField(max_length=225)


class Price(models.Model):
    title = models.CharField(max_length=225)
    size = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    


