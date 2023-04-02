from django.contrib import admin

from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = 'name', 'price', 'release_date', 'lte_exists', 'slug'


# Register your models here.
