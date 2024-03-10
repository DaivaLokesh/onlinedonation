from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("userhome",views.userhome,name="userhome"),
    path("viewdonations",views.viewdonations,name="viewdonations"),
    path("userchangepwd",views.userchangepwd, name="userchangepwd"),
   path("userupdatepwd",views.userupdatepwd,name="userupdatepwd"),
    path("contactmail/", views.contactmail, name="contactmail"),
    path("feedback",views.feedback,name="feedback"),
]