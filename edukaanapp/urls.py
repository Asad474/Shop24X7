from django.urls import path
from .views import *

urlpatterns = [ 
    path('', home, name = 'home'),
    path('signin/', sigin, name = 'signin'),
    path('signout/', signout, name = 'signout' ),
    path('signup/', signup, name = 'signup'),
    path('registerShop/', registerShop, name = 'registerShop'),
    path('addItem/<str:pk>/', addItem, name = 'addItem'),
    path('shop/<str:pk>/', shopdetails, name = 'shopdetails'),
]