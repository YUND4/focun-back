from django.urls import path
from .views import HealthCheckView

urlpatterns = [
    path('check/', HealthCheckView.as_view(), name='health-check'),
]
