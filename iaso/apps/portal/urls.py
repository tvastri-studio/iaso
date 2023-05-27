from django.urls import path

from . import views

app_name = "portal"

urlpatterns = [
    path("intake", views.IntakeWizard.as_view(), name="intake"),
]