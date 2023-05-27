import requests

from django.shortcuts import render
from django.conf import settings

from formtools.wizard.views import SessionWizardView

from . import forms

FORMS = [
    ("1", forms.IntakeFormPage1),
    ("2", forms.MedicationFormSet),
    ("3", forms.SupplamentFormSet),
    ("4", forms.ConditionFormSet),
    ("5", forms.IntakeFormPage5),
    ("6", forms.SurgeryFormSet),
    ("7", forms.InjuryFormSet),
    ("8", forms.IntakeFormPage8),
    ("9", forms.IntakeFormPage9),
    ("10", forms.IntakeFormPage10),
    ("11", forms.IntakeFormPage11),
]

TEMPLATES = {
    1: "portal/intake-page1.html",
    2: "portal/intake-page2.html",
    3: "portal/intake-page3.html",
    4: "portal/intake-page4.html",
    5: "portal/intake-page5.html",
    6: "portal/intake-page6.html",
    7: "portal/intake-page7.html",
    8: "portal/intake-page8.html",
    9: "portal/intake-page9.html",
    10: "portal/intake-page10.html",
    11: "portal/intake-page11.html",
}

# Create your views here.
class IntakeWizard(SessionWizardView):
    form_list = FORMS
    
    get_template_names = lambda self: TEMPLATES[int(self.steps.current)]

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        context['GOOGLE_PLACES_API_KEY'] = settings.GOOGLE_PLACES_API_KEY
        return context

    def done(self, form_list, **kwargs):
        form_data = self.get_all_cleaned_data()
        print(form_data)
        return render(self.request, 'portal/intake_submit.html', {'form_data': form_data})