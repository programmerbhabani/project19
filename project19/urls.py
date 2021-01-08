"""project19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from project19 import settings
from app19 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.DisplayIndex,name='main'),
    path('Admin_Login/',views.DisplayAdmin_Login,name='Admin_Login'),
    path('Admin_Login_checked/',views.DisplayAdmin_Login_checked,name='Admin_Login_checked'),
    path('Admin_home/',views.DisplayAdmin_home,name='Admin_home'),
    path('Admin_View_User/',views.DisplayAdmin_View_User,name='Admin_View_User'),
    path('Admin_View_Product/',views.DisplayAdmin_View_Product,name='Admin_View_Product'),
    path('Save_Product/',views.DisplaySave_Product,name='Save_Product'),

    path('Add_To_Cart/',views.DisplayAdd_To_Cart,name='Add_To_Cart'),
    path('In_Cart/',views.DisplayIn_Cart,name='In_Cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
