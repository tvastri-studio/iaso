from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("iaso.apps.auth.urls")),
    path("admin/", admin.site.urls),
    path("patients/", include("iaso.apps.patients.urls", namespace="patients")),
    path("portal/", include("iaso.apps.portal.urls", namespace="portal"))

]