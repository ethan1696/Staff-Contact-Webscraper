from django.urls import path
from .views import Routes


urlpatterns = [path("", Routes.as_view())]
