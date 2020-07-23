from django.urls import path
from . import views

urlpatterns = [
    
    

    path('contacts',views.contacts,name = 'contacts'),
    path('donate',views.donate,name = 'donate'),
    path('gallery',views.gallery,name = 'gallery'),
    path('team',views.team,name = 'team'),

    path('',views.home,name = 'home'),
    
    
    

]
