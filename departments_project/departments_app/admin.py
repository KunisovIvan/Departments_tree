from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Employees, Departments


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')


admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Departments, MPTTModelAdmin)
