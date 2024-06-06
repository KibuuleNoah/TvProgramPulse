from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
import random
import json

from .models import Program, UserPrograms, GENRE_CHOICES

# Create your views here.


class ProgramsHomeView(ListView):
    template_name = "home.html"
    # model = Program
    paginate_by = 10
    shuffled = False

    # def get(self, request, *args, **kwargs):
    # if p_filter := self.request.GET.get("p_filter"):
    # self.ordering = [p_filter]
    # return super().get(request, *args, **kwargs)
    def get_queryset(self):
        queryset = []
        if p_filter := self.request.GET.get("p_filter"):
            queryset = Program.objects.all().order_by(p_filter)
            self.shuffled = False
        elif not self.shuffled:
            queryset = list(Program.objects.all())
            # super().get_queryset()
            # queryset = list(queryset)
            random.shuffle(queryset)
            self.shuffled = True
            # self.shuffled_user_programs = queryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["p_filter"] = self.request.GET.get("p_filter")
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
            Program.objects.filter(**{f"{search_by}__icontains": search})
        )
        # print(self.object_list)
        return self.render_to_response(context=context)


class ProgramDetailView(TemplateView):
    template_name = "program-detail.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["program"] = get_object_or_404(Program, pk=pk)
        return context


class MyProgramListView(ListView):
    # model = UserPrograms
    template_name = "my-program-list.html"
    paginate_by = 10
    context_object_name = "user_programs"

    def get_queryset(self):
        queryset = UserPrograms.objects.filter(user=self.request.user)
        return queryset


class AddProgramView(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        program_id = json.loads(request.read()).get("program_id", 0)

        return JsonResponse({"success": True})
