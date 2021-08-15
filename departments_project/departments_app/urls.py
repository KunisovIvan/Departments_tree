from django.urls import path
from .views import Home, NewsByCategory

urlpatterns = [
    path('', Home.as_view(), name='employees_list'),
    path('departments/<str:slug>/', NewsByCategory.as_view(), name='departments'),
]
