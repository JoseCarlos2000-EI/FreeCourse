from rest_framework.generics import ListAPIView
from apps.course.serializer import CursoSerializer


class CursoListApiView(ListAPIView):
    serializer_class = CursoSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        name = self.request.GET.get('name')
        if name is not None or name.strip() != '':
            return model.objects.filter(status=True, name__icontains=name)
        return model.objects.filter(status=True)
