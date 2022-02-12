from django.urls import path
from apps.course.api import CursoListApiView
from apps.course.views import Home

urlpatterns = [
    #APIs Rest
    path('list_course', CursoListApiView.as_view(), name='list_course'),
    #Vistas
    path('', Home.as_view(), name='Home'),

]
