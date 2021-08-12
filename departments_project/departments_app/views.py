from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Employees, Departments


class Home(ListView):
    model = Employees
    template_name = 'departments_app/tables.html'
    context_object_name = 'employees'

    def get_context_data(self, *, object_list=None, **kwargs):
         context = super().get_context_data(**kwargs)
         context['departments'] = Departments.objects.all()
         return context

# class NewsByCategory(ListView):
#     template_name = 'departments_app/index.html'  # news_list
#     context_object_name = 'departments'  # object_list
#     # allow_empty = False #Для вывода ошибки 404 при пустом list
#     # paginate_by = 5
#
#     # extra_context = {'title': 'Категория'}
#
#     # Функция для передачи данных в шаблон
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['ancestors'] = get_object_or_404(Departments, slug=self.kwargs['slug']).get_ancestors(include_self=True)
#         return context
#
#
#     def get_queryset(self):
#         return get_object_or_404(Departments, slug=self.kwargs['slug']).get_descendants(include_self=True)

def employees_by_department(request, slug):
     department = get_object_or_404(Departments, slug=slug)
     departments = department.get_descendants(include_self=True)
     ancestors = department.get_ancestors(include_self=True)
     return render(request, 'departments_app/index.html', {'departments': departments,
                                                           'ancestors': ancestors})

