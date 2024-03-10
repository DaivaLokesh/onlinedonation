#from  django.contrib import admin
# from django.urls import path, include
# from .import views
#
# urlpatterns = [
#   # path('' , views.projecthomepage, name = 'projecthomepage'),
#   # path('donarhomepage',views.donarhomepage,name='donarhomepage'),
#   # path('userhomepage',views.userhomepage, name='userhomepage')
# ]
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

from django.urls import path
from .import views
urlpatterns = [
   path("adminhome",views.adminhome,name="adminhome"),
   path("logout",views.logout,name="logout"),
   path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
   path("adminchangepwd",views.adminchangepwd, name="adminchangepwd"),
   path("adminupdatepwd",views.adminupdatepwd,name="adminupdatepwd"),

   path("adminuser",views.adminuser,name="adminuser"),
   path("viewusers", views.viewusers, name="viewusers"),
   path("adduser",views.adduser,name="adduser"),
   path("insertuser",views.insertuser,name="insertuser"),
   path("deleteuser",views.deleteuser,name="deleteuser"),
   path("userdeletion/<int:id>",views.userdeletion,name="userdeletion"),


   path("admindonar", views.admindonar, name="admindonar"),
   path("viewdonars",views.viewdonars,name="viewdonars"),
   path("adddonar",views.addDonar,name="adddonar"),
   path("deletedonar", views.deletedonar, name="deletedonar"),
   path("donardeletion/<int:id>", views.donardeletion, name="donardeletion"),
   path("donarhome",views.donarhome,name="donarhome"),



   path("payment",views.payment,name="payment"),

]
