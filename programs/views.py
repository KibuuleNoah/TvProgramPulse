from django.http import HttpRequest, JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
import json

from .models import Program, UserPrograms, GENRE_CHOICES, Television

# Create your views here.


# def generate_genre():
#     return random.choice(GENRE_CHOICES.keys())
#
#
# def generate_tv():
#     return random.choice(Television.objects.all())
#
#
# def create():
#     programs = [
#         {
#             "name": "Program{i}",
#             "rating": 4.5,
#             "time": "12:00",
#             "duration": 60,
#             "days": "Mon Wed Fri",
#             "genre": generate_genre(),
#             "language": "English",
#             "description": "This is program 1",
#             "television": generate_tv(),
#         },
#             ]
#


class ProgramsHomeView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("auth-login")
    model = Program
    template_name = "home.html"
    paginate_by = 10

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "snippets/home-program-list.html"
        return self.template_name

    def get_queryset(self):
        if p_filter := self.request.GET.get("p_filter"):
            queryset = Program.objects.all().order_by(p_filter)
            return queryset
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["p_filter"] = self.request.GET.get("p_filter", "")
        context["program_genres"] = GENRE_CHOICES.keys()
        return context

    def post(self, request):
        search = request.POST.get("search")
        search_by = request.POST.get("search-by", "").lower()
        context = {}
        context["p_filter"] = ""
        context["program_genres"] = GENRE_CHOICES.keys()
        self.object_list = []
        context["object_list"] = list(
            Program.objects.filter(
                **{
                    f"{search_by}{'__icontains' if search_by != 'television' else '__name__icontains'}": search
                }
            )
        )
        # print(self.object_list)
        return self.render_to_response(context=context)


class ProgramDetailView(LoginRequiredMixin, TemplateView):
    template_name = "program-detail.html"
    login_url = reverse_lazy("auth-login")

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["program"] = get_object_or_404(Program, pk=pk)
        return context


class MyProgramListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("auth-login")
    template_name = "my-program-list.html"
    paginate_by = 10
    context_object_name = "user_programs"

    def get_queryset(self):
        queryset = UserPrograms.objects.filter(user=self.request.user)
        return queryset


class UserProgramCreateDeleteView(LoginRequiredMixin, View):
    login_url = reverse_lazy("auth-login")

    def post(self, request: HttpRequest, *args, **kwargs):
        program_id = json.loads(request.read()).get("program_id", 0)
        program = get_object_or_404(Program, pk=program_id)
        try:
            UserPrograms.objects.create(user=self.request.user, program=program)
        except:
            return JsonResponse(
                {"message": "Program already in your collection", "category": "error"}
            )
        return JsonResponse(
            {"message": "Program added successfully", "category": "success"}
        )

    def delete(self, request: HttpRequest, *args, **kwargs):
        user_program_id = json.loads(request.read()).get("program_id", 0)
        user_program = get_object_or_404(UserPrograms, pk=user_program_id)
        user_program.delete()
        return JsonResponse(
            {"message": "Program deleted successfully", "category": "success"}
        )
