from django.db.models.deletion import CASCADE, Collector
from djongo import models


class Seller(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=150, default=None)
    residence_city = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.name

class Location(models.Model):
    cityname = models.CharField(max_length=30)
    citystate = models.CharField(max_length=30)

    def __str__(self):
        return self.cityname

class Plant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    height = models.CharField(max_length=10)
    spacing = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    season = models.CharField(max_length=40)
    size = models.CharField(max_length=15, default=None)
    light_required = models.CharField(max_length=40, default=None)
    soil_requirements = models.CharField(max_length=50)
    growth_rate = models.CharField(max_length=40)
    location = models.ManyToManyField(Location, default=None)
    seller = models.ManyToManyField(Seller, default=None)


    def __str__(self):
        return self.name

    
class Fertilizer(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    weight = models.CharField(max_length=10)
    method_to_use = models.CharField(max_length=100)
    location = models.ForeignKey(Location, default=None, on_delete=models.CASCADE)
    seller = models.ManyToManyField(Seller, default=None)
    
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=30)
    gmail = models.CharField(max_length=50)
    phone = models.IntegerField()
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name