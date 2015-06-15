from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_in_menu', 'live', 'url')

admin.site.register(MenuItem, MenuItemAdmin)