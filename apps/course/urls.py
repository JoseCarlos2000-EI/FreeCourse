from django.urls import path
from apps.course.api import CursoListApiView

urlpatterns = [
    path('list_course/', CursoListApiView.as_view(), name='list_course'),
]
