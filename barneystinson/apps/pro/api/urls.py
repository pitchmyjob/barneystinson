from rest_framework.routers import DefaultRouter

from django.conf.urls import url

from .views import ProViewSet, ProRegisterAPIView


router = DefaultRouter()
router.register('pros', ProViewSet, base_name='pro')

urlpatterns = router.urls + [
    url(r'^pros/register', ProRegisterAPIView.as_view()),
]
