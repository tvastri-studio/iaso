from django.shortcuts import render
from ..dashboard.views import dashboard

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return dashboard(request)

    form  = None

    context = {
        "form": form
    }

    return render(request, 'auth/login.html', context=context)