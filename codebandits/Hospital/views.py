from django.shortcuts import render
from .models import State,City,medicine,Hospital
# Create your views here.
def Home(request):
    hospitallist=list(Hospital.objects.all())
    return render(request,'home.html',{'hl':hospitallist})