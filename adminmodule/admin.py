from django.contrib import admin

from .models import Admin, Donar, User, Donation, Payment

# Register your models here.
admin.site.register(Admin)
admin.site.register(Donar)
admin.site.register(User)
admin.site.register(Payment)
admin.site.register(Donation)
