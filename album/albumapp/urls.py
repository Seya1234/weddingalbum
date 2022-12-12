from . import views
from django.urls import path
app_name='albumapp'
urlpatterns =[
    path('',views.home, name='home'),
    path('eng/',views.eng, name='engagement.html'),
    path('mk_sreya/',views.mk_sreya, name='mk_sreya.html'),
    path('mk_sethu/',views.mk_sethu, name='mk_sethu.html'),
    path('wedding/',views.wedding, name='wedding.html')
]

