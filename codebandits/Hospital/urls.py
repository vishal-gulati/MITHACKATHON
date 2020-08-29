from django.urls import path,include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('Index',views.Index,name='Index')
    path('Test',views.Graph,name='graph')
]
