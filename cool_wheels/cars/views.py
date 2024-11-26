from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import Car
from .forms import CommentForm


# Create your views here.
# @method_decorator(login_required, name="dispatch")
class CarDetails(DetailView):
    model = Car
    template_name = "details.html"
    pk_url_kwarg = "id"

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()

        context["comments"] = comments
        context["comment_form"] = comment_form
        return context
