from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.job_list, name="job-list"),
    path('<int:id>', views.details, name="details"),
]