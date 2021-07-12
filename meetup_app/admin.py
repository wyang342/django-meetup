from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Group, Event

admin.site.register(User, UserAdmin)
admin.site.register(Group)
admin.site.register(Event)
