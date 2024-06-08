from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, UserLoginForm
from .models import CustomUser
from programs.models import Program, UserPrograms

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
        username = form.cleaned_data["username"]
        if username.istitle() and username.find(" ") == -1:
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
        return self.render_to_response(
            self.get_context_data(
                form=form,
                invalid=True,
                username_error="Username first letter must be upper and nospace in it",
            )
        )


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


class DashBoard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"
    login_url = reverse_lazy("auth-login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_programs = UserPrograms.objects.filter(user=self.request.user)
        ongoing = list(
            filter(lambda x: x.program.get_status == "Ongoing", user_programs)
        )
        upcoming = list(
            filter(lambda x: x.program.get_status == "Upcoming", user_programs)
        )

        ended = list(filter(lambda x: x.program.get_status == "Ended", user_programs))

        context["ongoing"] = ongoing[:3]
        context["upcoming"] = upcoming[:3]
        context["ended"] = ended[:3]
        context["ongoing_len"] = len(ongoing)
        context["upcoming_len"] = len(upcoming)
        context["ended_len"] = len(ended)
        context["user_programs"] = list(user_programs)
        return context


class LogOutUser(LoginRequiredMixin, View):
    login_url = reverse_lazy("auth-login")

    def get(self, request):
        logout(request)
        return redirect("auth-login")
