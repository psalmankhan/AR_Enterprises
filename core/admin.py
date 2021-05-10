from django.contrib import admin
from .models import Order, Contact

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'total', 'brand')
    list_display_links = ('name', 'email')
    search_fields = ('name', 'email', 'brand')
    list_per_page = 25

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_display_links = ('name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 25
