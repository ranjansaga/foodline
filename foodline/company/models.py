from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    customer=models.ForeignKey(User)
    contact_no=models.IntegerField(max_length = 10)
    address=models.TextField()
    
class Company(models.Model):
    company=models.ForeignKey(User)
    company_name = models.CharField(max_length = 30)
    address=models.TextField()
    home_delivery=models.BooleanField()
    lodging=models.BooleanField()
    cuisine=models.CharField(max_length = 30)
    contact_no=models.IntegerField(max_length = 10)
    

class Recipes(models.Model):
    name=models.CharField(max_length = 30)
    ingredients=models.TextField()
    description=models.TextField()


class CustomerChoice(models.Model):

    cuisine=models.CharField(max_length = 30)
    home_delivery=models.BooleanField()
    lodging=models.BooleanField()


class UserProfile(models.Model):
    user=models.ForeignKey(User,unique=True)
    user_type=models.CharField(max_length=10)


class Reviews(models.Model):
    voteup = models.IntegerField(null=True,default=0)
    votedown = models.IntegerField(null=True,default=0)
    reviews = models.CharField(max_length = 30,null=True)
    



