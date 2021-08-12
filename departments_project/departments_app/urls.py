from django.urls import path
from .views import Home, employees_by_department

urlpatterns = [
    path('', Home.as_view(), name='employees_list'),
    path('departments/<str:slug>/', employees_by_department, name='departments'),
]
