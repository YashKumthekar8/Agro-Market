from django.db.models.deletion import Collector
from djongo import models


class Seller(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    # flower_id = models.ForeignKey(to=)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=30)
    gmail = models.CharField(max_length=50)
    phone = models.IntegerField()

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
    season = models.CharField(max_length=30)
    soil_requirements = models.CharField(max_length=30)
    growth_rate = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    
class Fertilizer(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    weight = models.CharField(max_length=10)
    method_to_use = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
