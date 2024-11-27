from django.urls import path
from .views import CarDetails, buy_car

urlpatterns = [
    path("details/<int:id>", CarDetails.as_view(), name="car_details"),
    path("buy/<int:id>", buy_car, name="buy_car"),
]
