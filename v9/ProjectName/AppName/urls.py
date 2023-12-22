
from django.urls import path
from AppName import views
urlpatterns = [
    path('',views.home,name="home"),
    path('managetaskadd/',views.managetaskadd,name="managetaskadd"),
    path('managetaskdelete/',views.managetaskdelete,name="managetaskdelete"),
    path('managetaskupdate/',views.managetaskupdate,name="managetaskupdate"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('userlogin/',views.user_login,name="userlogin"),
]
