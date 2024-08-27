from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Application
from .serializers import ApplicationSerializer

# Create your views here.

class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user.student)
