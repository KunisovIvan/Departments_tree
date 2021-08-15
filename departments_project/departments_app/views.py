from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Employees, Departments


class Home(ListView):
    model = Employees
    template_name = 'departments_app/index.html'
    context_object_name = 'employees'
    paginate_by = 10
    queryset = Employees.objects.select_related('department')

    def get_context_data(self, *, object_list=None, **kwargs):
         context = super().get_context_data(**kwargs)
         context['count'] = len(Employees.objects.all())
         return context


class NewsByCategory(ListView):
    template_name = 'departments_app/index.html'  # news_list
    context_object_name = 'employees'  # object_list
    # allow_empty = False #Для вывода ошибки 404 при пустом list
    paginate_by = 10

    # extra_context = {'title': 'Отделы'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ancestors'] = get_object_or_404(Departments, slug=self.kwargs['slug']).get_ancestors(include_self=True)
        context['count'] = len(Employees.objects.filter(department__in=Departments.objects.get(slug=self.kwargs['slug']).get_descendants(include_self=True)))
        return context


    def get_queryset(self):
         return Employees.objects.filter(department__in=Departments.objects.get(slug=self.kwargs['slug']).get_descendants(include_self=True)).select_related('department')


