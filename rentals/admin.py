from django.contrib import admin

# Register your models here.

from rentals.models import UserProfile,Property

admin.site.register(UserProfile)
admin.site.register(Property)