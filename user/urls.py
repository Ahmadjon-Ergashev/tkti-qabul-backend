from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from dj_rest_auth.views import LoginView

from .views import (
    RegisterView,
    StudentViewSet,
)

router = DefaultRouter()
router.register(r'student', StudentViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]
