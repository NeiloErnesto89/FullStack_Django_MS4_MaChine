from django.contrib import admin
from .models import Mess, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Mess)  #simply registered Mess on admin panel
