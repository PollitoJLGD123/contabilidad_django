from django.urls import path
from seguridadApp.views import homePage, salir,ingresar_login,registrarse

urlpatterns = [
    path('', ingresar_login, name='login'),
    path('registro/', registrarse, name='regis'),
    path('home/<str:username>/', homePage, name='homePage'),
    path('logout/',salir,name="logout"),
]
