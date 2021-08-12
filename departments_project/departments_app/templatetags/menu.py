from django import template
from departments_app.models import Departments

register = template.Library()

@register.inclusion_tag('departments_app/include/menu.html')

def show_menu():
    departments = Departments.objects.all()
    return {"departments": departments}


