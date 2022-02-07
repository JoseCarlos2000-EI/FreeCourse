from rest_framework.generics import ListAPIView
from apps.course.serializer import CursoSerializer


class CursoListApiView(ListAPIView):
    serializer_class = CursoSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(status=True)
