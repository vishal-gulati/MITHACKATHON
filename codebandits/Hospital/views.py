from django.shortcuts import render
from .models import State,City,Hospital
from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib,base64
# Create your views here.
def Home(request):
    if(request.method=='POST'):
        citylist=list(City.objects.all())
        hospitallist=list(Hospital.objects.all())
        beds=[0,0,0]
        bedsa=[0,0,0]
        bedsc=[0,0,0]
        bedsl=['l1beds','l2beds','l3beds']
        hosp=[]
        
        for c in hospitallist:
            n=c.City.Name
            beds[0]=beds[0]+c.l1beds
            beds[1]=beds[1]+c.l2beds
            beds[2]=beds[2]+c.l3beds
            bedsa[0]=bedsa[0]+c.l1bedso
            bedsa[1]=bedsa[1]+c.l2bedso
            bedsa[2]=bedsa[2]+c.l3bedso
            
            if request.POST.get("city")==n:
                hosp.append(c)
        if request.POST.get("graph")=="True":

            bedsa[0]=beds[0]-bedsa[0]
            bedsa[1]=beds[1]-bedsa[1]
            bedsa[2]=beds[2]-bedsa[2]
            plt.pie(beds, labels =bedsl)
            fig=plt.gcf()
            fig.savefig('Hospital/static/Hospital/a.png')
            plt.pie(bedsa, labels =bedsl)
            fig=plt.gcf()
            fig.savefig('Hospital/static/Hospital/b.png')
            
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
