from django import forms
from .models import Patient

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, MultiField

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "email", "phone_number", "address"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.method = "POST"
        self.helper.form_class = "form-inline"

        self.helper.layout = Layout(
            Div(
                "Create a patient",
                Div(
                    "first_name",
                    "last_name",
                ),
                "email",
                "phone_number",
                "address"
            ),
            Submit("submit", "Create")
        )