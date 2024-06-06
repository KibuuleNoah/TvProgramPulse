from django.urls import path
from .views import (
    ProgramsHomeView,
    ProgramDetailView,
    MyProgramListView,
    AddProgramView,
)

urlpatterns = [
    path("", ProgramsHomeView.as_view(), name="home"),
    path("add/program/", AddProgramView.as_view(), name="add-program"),
    path("program/<int:pk>/", ProgramDetailView.as_view(), name="program-detail"),
    path("my-programs/", MyProgramListView.as_view(), name="my-programs"),
]
