"""
URL configuration for onlinedonationsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.demofunction,name="demofunction"),
    path('donar/',include('donar.urls')),
    path('user/',include('usermodule.urls')),
    path("demo1",views.demofunction,name="demo"),
     path("home",views.homefunction,name="home"),
    path("about",views.aboutfunction,name="about"),
   path("login",views.loginfunction,name="login"),
   path("contact",views.contactfunction,name="contact"),
   path("userlogin",views.userlogin,name="userlogin"),
    path("donarlogin",views.donarlogin,name="donarlogin"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path("checkdonarlogin",views.checkdonarlogin,name="checkdonarlogin"),


    path("",include("adminmodule.urls")),
    path("",include("donar.urls")),
    path("",include("usermodule.urls")),
]+  static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
