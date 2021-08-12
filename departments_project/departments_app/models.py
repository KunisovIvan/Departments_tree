from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Employees(models.Model):
      name = models.CharField(max_length=120, verbose_name='Ф.И.О')
      position = models.CharField(max_length=120, verbose_name='Должность')
      employment_date = models.DateField(verbose_name='Дата приема на работу')
      salary = models.FloatField(verbose_name='Зарплата')
      department = TreeForeignKey('Departments', on_delete=models.PROTECT, null=True, blank=True, related_name='employees', verbose_name='Отдел')

      def __str__(self):
        return self.name



class Departments(MPTTModel):
      title = models.CharField(max_length=50, unique=True, verbose_name='Название')
      parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', db_index=True, verbose_name='Родительский отдел')
      slug = models.SlugField()

      class MPTTMeta:
          order_insertion_by = ['title']

      def get_absolute_url(self):
          return reverse('departments', kwargs={'slug': self.slug})


      def __str__(self):
        return self.title