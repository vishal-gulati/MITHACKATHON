from django.db import models

# Create your models here.
class State(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return '%s' % (self.Name)
class City(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    State=models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.Name)
class medicine(models.Model):
    Remdisivir=models.IntegerField()
    FabiFlu=models.IntegerField()
    def __str__(self):
        return '%s' % ('Medicine')
class Hospital(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    City=models.ForeignKey(City, on_delete=models.CASCADE)
    l1beds=models.IntegerField()
    l1bedso=models.IntegerField()
    l2beds=models.IntegerField()
    l2bedso=models.IntegerField()
    l3beds=models.IntegerField()
    l3bedso=models.IntegerField()
    ppe=models.IntegerField()
    med=models.ForeignKey(medicine,on_delete=models.CASCADE)
    Mob=models.CharField(max_length=12)
    email=models.EmailField(max_length=254)
    def __str__(self):
        return '%s' % (self.Name)