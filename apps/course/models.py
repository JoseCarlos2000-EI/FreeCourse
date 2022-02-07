from django.db import models


class Curso(models.Model):
    name = models.CharField(verbose_name='Nombre',max_length=100, blank=False)
    description = models.TextField(verbose_name='Descripción', blank=False)
    author = models.CharField(verbose_name='Autor del curso', max_length=100, blank=False)
    url = models.CharField(verbose_name='URL', max_length=100, blank=True)
    image = models.ImageField(verbose_name='Imagen', blank=False)
    status = models.BooleanField(verbose_name='Estado', default=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
