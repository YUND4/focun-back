from django.contrib import admin
from .models import User, Admin, Authenticable, Profile

admin.site.register(Authenticable)
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Profile)