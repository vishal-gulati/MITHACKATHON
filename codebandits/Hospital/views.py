from django.shortcuts import render
from .models import State,City,Hospital
# Create your views here.
def Home(request):
    if(request.method=='POST'):
        citylist=list(City.objects.all())
        hospitallist=list(Hospital.objects.all())
        hosp=[]
        for c in hospitallist:
            n=c.City.Name
            if request.POST.get("city")==n:
                hosp.append(c)
        return render(request,'index.html',{'hl':hosp,'cl':citylist})
    else:       
        hospitallist=list(Hospital.objects.all())
        citylist=list(City.objects.all())
        return render(request,'index.html',{'hl':hospitallist,'cl':citylist})

def Index(request):
    if(request.method=='POST'):
        user=request.user
        citylist=list(City.objects.all())
        hospitallist=list(Hospital.objects.all())
        hosp=[]
        for c in hospitallist:
            n=c.City.Name
            if request.POST.get("city")==n:
                hosp.append(c)
        return render(request,'hospital.html',{'hl':hospitallist,'b':user,'cl':citylist})
    else:
        user=request.user
        hospitallist=list(Hospital.objects.all())
        citylist=list(City.objects.all())
        return render(request,'hospital.html',{'hl':hospitallist,'b':user,'cl':citylist})
    