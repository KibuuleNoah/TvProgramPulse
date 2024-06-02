from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate
from .forms import CustomUserCreationForm, UserLoginForm
from .models import CustomUser

# Create your views here.


class UserSignupView(FormView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if kwargs.get("invalid", None) != True:
            context["form"] = self.form_class
        return context

    def form_invalid(self, form):
        print(form["username"].value)
        return self.render_to_response(self.get_context_data(form=form, invalid=True))

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]

        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = "login.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user_exists = CustomUser.objects.filter(username=username).first()

        if user_exists:
            user = authenticate(
                self.request,
                username=username,
                password=password,
            )
            if user:
                login(self.request, user)
                return super().form_valid(form)
            return self.render_to_response(
                self.get_context_data(
                    username=username, message="Wrong password for that user name"
                )
            )
        return self.render_to_response(
            self.get_context_data(message="User name doesn't exists")
        )


class DashBoard(TemplateView):
    template_name = "dashboard.html"


def logout_user(request):
    logout(request)
    return redirect("auth-login")
