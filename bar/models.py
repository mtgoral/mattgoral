from django.db import models

class Bar(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Drink(models.Model):
    bar = models.ForeignKey(Bar)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name