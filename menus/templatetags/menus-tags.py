from django import template
from menus.models import Menu
from django.shortcuts import get_object_or_404

register = template.Library()


@register.inclusion_tag('navbar.html')
def main_menu(calling_page=None):
    menu = get_object_or_404(Menu, name='main')
    return {
        'menu': menu
    }


