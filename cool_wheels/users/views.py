from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "User Registered Succesfully")
            return redirect("homepage")
    else:
        register_form = RegistrationForm()
    return render(request, "sign_up.html", {"form": register_form, "type": "Register"})


class UserLoginView(LoginView):
    template_name = "sign_up.html"

    def get_success_url(self):
        return reverse_lazy("homepage")  # change to profile page later

    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Login information is incorrect")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context


def user_logout(request):
    logout(request)
    return redirect("login_page")
