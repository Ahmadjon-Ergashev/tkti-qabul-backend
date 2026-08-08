from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

# Create your views here.
from .models import News
from .serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_queryset(self):
        if self.request.method == 'GET':
            return self.queryset.order_by('-created_at')
        return self.queryset

