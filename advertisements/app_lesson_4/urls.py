from django.urls import path
from .views import les

urlpatterns = [
    path('', les)
]
