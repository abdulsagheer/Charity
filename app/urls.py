from django.urls import path
from .views import index,info,home

urlpatterns = [
    path('',home,name='home'),
    path('donate',index,name='donate'),
    path('info',info,name='info'),
   
    
]