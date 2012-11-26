from django.db import models
from django.forms import ModelForm

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
        
class Order(models.Model):
    bar = models.ForeignKey(Bar)
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    drink = models.ForeignKey(Drink)
    quantity = models.IntegerField()
    
class OrderForm(ModelForm):
    class Meta:
        model = OrderItem