from django.contrib import admin
from django.urls import path
from Firstpage import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/',views.show),
    path('gm/',views.gm),
    path('ga/',views.ga),
    path('ge/',views.ge),
    path('display/',views.display),   
]