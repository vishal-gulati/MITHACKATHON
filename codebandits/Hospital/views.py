from django.shortcuts import render
from .models import State,City,Hospital
# Create your views here.
def Home(request):
    hospitallist=list(Hospital.objects.all())
    return render(request,'index.html',{'hl':hospitallist})