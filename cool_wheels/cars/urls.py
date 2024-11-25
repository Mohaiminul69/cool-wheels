from django.urls import path
from .views import CarDetails

urlpatterns = [
    path("details/<int:id>", CarDetails.as_view(), name="car_details"),
]
