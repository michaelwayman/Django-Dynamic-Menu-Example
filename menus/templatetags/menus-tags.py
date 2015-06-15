from django import template
from menus.models import MenuItem

register = template.Library()


@register.inclusion_tag('navbar.html', takes_context=True)
def top_menu(context, calling_page=None):
    menu_items = MenuItem.objects.filter(
        live=True,
        show_in_menu=True
    ).order_by('order')
    return {
        'menu_items': menu_items,
    }