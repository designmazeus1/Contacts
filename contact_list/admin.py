from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact admin"""
    list_display = ("id","name", "phone", "updated", "user")
    list_display_links = ("name",)