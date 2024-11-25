from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import Car


# Create your views here.
@method_decorator(login_required, name="dispatch")
class CarDetails(DetailView):
    model = Car
    template_name = "details.html"
    pk_url_kwarg = "id"
