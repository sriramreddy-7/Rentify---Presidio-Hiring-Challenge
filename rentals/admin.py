from django.contrib import admin

# Register your models here.

from rentals.models import UserProfile,Property,Like,PropertyPhoto

admin.site.register(UserProfile)
admin.site.register(Property)
admin.site.register(Like)
admin.site.register(PropertyPhoto)