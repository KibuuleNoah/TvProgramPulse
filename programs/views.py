from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
import random
import json

from .models import Program

# Create your views here.


class ProgramsHomeView(ListView):
    template_name = "home.html"
    model = Program
    paginate_by = 10

    shuffled_queryset = None

    def get_queryset(self):
        if not self.shuffled_queryset:
            queryset = super().get_queryset()
            queryset = list(queryset)
            random.shuffle(queryset)
            self.shuffled_queryset = queryset
        return self.shuffled_queryset


class ProgramDetailView(TemplateView):
    template_name = "program-detail.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["program"] = get_object_or_404(Program, pk=pk)
        return context


class MyProgramListView(TemplateView):
    template_name = "my-program-list.html"


class AddProgramView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        program_id = json.loads(request.read()).get("program_id", 0)

        return JsonResponse({"success": True})
