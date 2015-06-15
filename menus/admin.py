from django.contrib import admin
from .models import MenuItem, Menu, MenuGroup


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']


class MenuItemInline(admin.TabularInline):
    model = MenuItem


class MenuGroupAdmin(admin.ModelAdmin):
    inlines = [
        MenuItemInline,
    ]


class MenuGroupInline(admin.TabularInline):
    model = MenuGroup
    extra = 1


class MenuAdmin(admin.ModelAdmin):

    inlines = [
        MenuGroupInline,
    ]

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuGroup, MenuGroupAdmin)
admin.site.register(Menu, MenuAdmin)
