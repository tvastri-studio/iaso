from django.shortcuts import render
from django.conf import settings


from django.core.mail import send_mail

from .forms import PatientCreateForm

# Create your views here.
def index(request):
    return render(request, "patients/index.html")

def create(request):
    if request.method == "POST":
        form = PatientCreateForm(request.POST)

        if form.is_valid():
            patient = form.save()

            send_mail(
                "Fill out your patient intake form!",
                f"Thank you for your interest in the Shrivatsa Center. Here is the link to your personalized intake form: http://localhost:8000/portal/intake?id={patient.uuid}",
                settings.EMAIL_HOST_USER,
                [patient.email]
            )

            return render(request, "patients/index.html")
        else:
            context = {
                "form": form
            }

            return render(request, "patients/create.html", context=context)

    context = {
        "form": PatientCreateForm()
    }

    return render(request, "patients/create.html", context=context)