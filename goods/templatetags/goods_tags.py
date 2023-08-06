from django import template
from goods.models import *

register = template.Library()


@register.inclusion_tag("goods/tags/sidebar.html")
def show_sidebar(category_selected, subcategory_selected=None):
    categories = Category.objects.all()

    context = {
        "categories": categories,
        "category_selected": category_selected,
        "subcategory_selected": subcategory_selected,
    }
    return context
