from django.conf.urls import url

from .views import ProMeAPIView


urlpatterns = [
    url(r'^pro/me', ProMeAPIView.as_view(), name="pro"),
]
