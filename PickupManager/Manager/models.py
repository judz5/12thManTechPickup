from django.db import models

# Create your models here.

class Cubby(models.Model):
    location = models.CharField(max_length=2)
    # also some way to track all orders assosciated with

    def __str__(self):
        return self.location

class OrdType(models.Model):
    type = models.CharField(max_length=2)

    def __str__(self):
        return self.type

class Order(models.Model):
    name = models.CharField(max_length=100)
    datePlaced = models.DateField()
    complete = models.BooleanField()
    cubby = models.ForeignKey(Cubby, on_delete=models.CASCADE)
    orderType = models.ForeignKey(OrdType, on_delete=models.CASCADE)
    pickupDate = models.DateField()

    def __str__(self):
        return self.name