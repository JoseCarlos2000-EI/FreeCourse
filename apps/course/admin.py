from django.contrib import admin
from apps.course.models import Curso


class AdminCourse (admin.ModelAdmin):
    list_display = ('name', 'author', 'status')


admin.site.register(Curso, AdminCourse)
