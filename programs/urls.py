from django.urls import path
from .views import (
    ProgramsHomeView,
    ProgramDetailView,
    MyProgramListView,
    UserProgramCreateDeleteView,
)

urlpatterns = [
    path("", ProgramsHomeView.as_view(), name="home"),
    path(
        "program-cd/",
        UserProgramCreateDeleteView.as_view(),
        name="program-create-delete",
    ),
    path("program/<int:pk>/", ProgramDetailView.as_view(), name="program-detail"),
    path("my-programs/", MyProgramListView.as_view(), name="my-programs"),
]
