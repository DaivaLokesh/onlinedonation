from django.urls import path
from .import views
urlpatterns=[
    path("signup",views.signup,name="signup"),
   path("donarchangepwd",views.donarchangepwd, name="donarchangepwd"),
   path("donarupdatepwd",views.donarupdatepwd,name="donarupdatepwd"),
    path("donaruser",views.donaruser,name="donaruser"),
    path("donorhome",views.donorhome,name="donorhome"),
    path("displaydonaruser",views.displaydonaruser,name="displaydonaruser"),
    path("checkdonorlogin",views.checkdonorlogin,name="checkdonorlogin"),
    path("donardonations",views.donardonations,name="donardonations"),
    path("payment_status",views.paymentstatus,name="payment_status"),
]