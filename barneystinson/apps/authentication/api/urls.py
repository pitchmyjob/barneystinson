from django.conf.urls import url

from .views import AuthProLoginAPIView


urlpatterns = [
    url(r'^auth/pro/login', AuthProLoginAPIView.as_view()),
]
