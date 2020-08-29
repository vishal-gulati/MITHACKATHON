from django.db import models

# Create your models here.
class State(models.Model):
    Name=models.CharField(max_length=100,unique=True)
class City(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    State=models.ForeignKey(State, on_delete=models.CASCADE)
class medicine(models.Model):
    Remdisivir=models.IntegerField()
    FabiFlu=models.IntegerField()
class Hospital(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    City=models.ForeignKey(City, on_delete=models.CASCADE)
    l1beds=models.IntegerField()
    l2beds=models.IntegerField()
    l3beds=models.IntegerField()
    ppe=models.IntegerField()
    med=models.ForeignKey(medicine,on_delete=models.CASCADE)
    Mob=models.CharField(max_length=12)
    email=models.EmailField(max_length=254)
