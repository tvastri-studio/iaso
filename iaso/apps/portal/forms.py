from django import forms
from .models import IntakeForm, Medication, Supplament, Condition, Surgery, Injury

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, HTML, Div
from crispy_bootstrap5.bootstrap5 import FloatingField

class MedicationIntakeForm(forms.ModelForm):
    medicine = forms.CharField(max_length=100,required=False, label="Medicine Name")
    dose = forms.CharField(max_length=100,required=False, label="Dosage (mg, ml, etc.)")
    frequency = forms.CharField(max_length=100,required=False, label="Frequency (daily, weekly, etc.)")
    duration = forms.CharField(max_length=100,required=False, label="About how long ago did you start?")

    class Meta:
        model = Medication
        fields = [
            "medicine",
            "dose",
            "frequency",
            "duration",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            HTML('<h3>Medication {{forloop.counter}}</h3>'),
            Row(
                Column(FloatingField('medicine'), css_class='form-group col-md-6 mb-0'),
                Column(FloatingField('dose'), css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column(FloatingField('frequency'), css_class='form-group col-md-6 mb-0'),
                Column(FloatingField('duration'), css_class='form-group col-md-6 mb-0'),
            )
        )

MedicationFormSet = forms.modelformset_factory(
    Medication,
    form=MedicationIntakeForm,
)

class SupplamentIntakeForm(forms.ModelForm):
    name = forms.CharField(max_length=100,required=False, label="Name")
    dose = forms.CharField(max_length=100,required=False, label="Dosage (tsp, drops, etc.)")
    frequency = forms.CharField(max_length=100,required=False, label="Frequency (daily, weekly, etc.)")
    duration = forms.CharField(max_length=100,required=False, label="About how long ago did you start?")

    class Meta:
        model = Medication
        fields = [
            "name",
            "dose",
            "frequency",
            "duration",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            HTML('<h3>Supplament {{forloop.counter}}</h3>'),
            Row(
                Column(FloatingField('name'), css_class='form-group col-md-6 mb-0'),
                Column(FloatingField('dose'), css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column(FloatingField('frequency'), css_class='form-group col-md-6 mb-0'),
                Column(FloatingField('duration'), css_class='form-group col-md-6 mb-0'),
            )
        )

SupplamentFormSet = forms.modelformset_factory(
    Supplament,
    form=SupplamentIntakeForm,
    extra=1
)

class ConditionIntakeForm(forms.ModelForm):
    name = forms.ChoiceField(choices=Condition.CONDITIONS, required=False, label="Condition")
    when_diagnosed = forms.CharField(max_length=100,required=False, label="About when were you diagnosed?")

    class Meta:
        model = Condition
        fields = [
            "name",
            "when_diagnosed",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Column(FloatingField('name'), css_class='mx-2'),
                Column(FloatingField('when_diagnosed'), css_class='mx-2'),
            )
        )

ConditionFormSet = forms.modelformset_factory(
    Condition,
    form=ConditionIntakeForm,
)

class SurgeryIntakeForm(forms.ModelForm):
    name = forms.CharField(max_length=100,required=False, label="Name")
    when = forms.CharField(max_length=100,required=False, label="When did you have this surgery?")

    class Meta:
        model = Condition
        fields = [
            "name",
            "when",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Div(
                Column(FloatingField('name'), css_class='mx-2'),
                Column(FloatingField('when'), css_class='mx-2'),
            )
        )

SurgeryFormSet = forms.modelformset_factory(
    Surgery,
    form=SurgeryIntakeForm,
)

class InjuryIntakeForm(forms.ModelForm):
    name = forms.CharField(max_length=100,required=False, label="Name")
    when = forms.CharField(max_length=100,required=False, label="When did you have this injury?")

    class Meta:
        model = Condition
        fields = [
            "name",
            "when",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Div(
                Column(FloatingField('name'), css_class='mx-2'),
                Column(FloatingField('when'), css_class='mx-2'),
            )
        )

InjuryFormSet = forms.modelformset_factory(
    Injury,
    form=InjuryIntakeForm,
)

class IntakeFormPage1(forms.ModelForm):
    full_name = forms.CharField(max_length=100, required=True, label="Full Name")
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(required=True, label="Age")
    phone_number = forms.CharField(max_length=100, required=False, label="Phone Number")
    email = forms.EmailField(required=False, label="Email")

    address_line_1 = forms.CharField(max_length=100, required=True, label="Address Line 1")
    address_line_2 = forms.CharField(max_length=100, required=False, label="Address Line 2 (optional)")
    city = forms.CharField(max_length=100, required=True, label="City")
    state = forms.CharField(max_length=20, required=True, label="State")
    zip_code = forms.CharField(max_length=20, required=True, label="Zip")

    emergency_contact_name = forms.CharField(max_length=100, required=True, label="Emergency Contact Name")
    emergency_contact_phone_number = forms.CharField(max_length=100, required=True, label="Phone Number")
    emergency_contact_relationship = forms.CharField(max_length=100, required=True, label="Relationship to you")

    primary_care_provider = forms.CharField(max_length=100, required=False, label="Primary Care Provider")
    other_care = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 30}), label="Who else are you seeing for your health needs? (optional)")

    takes_perscribed_medication = forms.BooleanField(required=False, label="Do you take any prescribed medication?")
    takes_herbal_medicine = forms.BooleanField(required=False, label="Have you ever taken any herbal medicine?")
    has_done_shiatsu = forms.BooleanField(required=False, label="Have you ever done shiatsu?")
    has_cat = forms.BooleanField(required=False, label="Do you have a cat?")

    class Meta:
        model = IntakeForm
        fields = [
            "full_name",
            "date_of_birth",
            "age",
            "phone_number",
            "email",

            "address_line_1",
            "address_line_2",
            "city",
            "state",
            "zip_code",

            "emergency_contact_name",
            "emergency_contact_phone_number",
            "emergency_contact_relationship",

            "primary_care_provider",
            "other_care",

            "takes_perscribed_medication",
            "takes_herbal_medicine",
            "has_done_shiatsu",
            "has_cat",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset(
                'Personal Information',
                FloatingField('full_name'),
                Row(
                    Column(FloatingField('date_of_birth'), css_class='form-group col-md-6 mb-0'),
                    Column(FloatingField('age'), css_class='form-group col-md-6 mb-0'),
                ),
                Row(
                    Column(FloatingField('phone_number'), css_class='form-group col-md-6 mb-0'),
                    Column(FloatingField('email'), css_class='form-group col-md-6 mb-0'),
                ),
                HTML('<h3>Address</h3>'),
                FloatingField('address_line_1'),
                FloatingField('address_line_2'),
                Row(
                    Column(FloatingField('city'), css_class='form-group col-md-6 mb-0'),
                    Column(FloatingField('state'), css_class='form-group col-md-3 mb-0'),
                    Column(FloatingField('zip_code'), css_class='form-group col-md-3 mb-0'),
                ),
            css_class='rounded-3 p-3'
            ),

            Fieldset(
                'Emergency Contact',
                FloatingField('emergency_contact_name'),
                Row(
                    Column(FloatingField('emergency_contact_phone_number'), css_class='form-group col-md-6 mb-0'),
                    Column(FloatingField('emergency_contact_relationship'), css_class='form-group col-md-6 mb-0'),
                ),
            css_class='rounded-3 p-3'
            ),

            Fieldset(
                'Current Care',
                FloatingField('primary_care_provider'),
                FloatingField('other_care'),
                'takes_perscribed_medication',
                'takes_herbal_medicine',
                'has_done_shiatsu',
                'has_cat',
            css_class='rounded-3 p-3'
            )
        )

class IntakeFormPage5(forms.ModelForm):
    allergies = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Allergies (optional)")
    other_conditions = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Other conditions (optional)")

    class Meta:
        model = IntakeForm
        fields = [
            "allergies",
            "other_conditions",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset(
                'Other Conditions',
                FloatingField('allergies'),
                FloatingField('other_conditions'),
            css_class='rounded-3 p-3'
            )
        )

class IntakeFormPage8(forms.ModelForm):
    mother = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Mother")
    father = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Father")
    maternal_grandmother = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Maternal Grandmother")
    maternal_grandfather = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Maternal Grandfather")
    paternal_grandmother = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Paternal Grandmother")
    paternal_grandfather = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Paternal Grandfather")
    sisters = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Sisters")
    brothers = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Brothers")
    children = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Children")
    extended_family = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Extended Family")

    class Meta:
        model = IntakeForm
        fields = [
            "mother",
            "father",
            "maternal_grandmother",
            "maternal_grandfather",
            "paternal_grandmother",
            "paternal_grandfather",
            "sisters",
            "brothers",
            "children",
            "extended_family",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            FloatingField('mother'),
            FloatingField('father'),
            FloatingField('maternal_grandmother'),
            FloatingField('maternal_grandfather'),
            FloatingField('paternal_grandmother'),
            FloatingField('paternal_grandfather'),
            FloatingField('sisters'),
            FloatingField('brothers'),
            FloatingField('children'),
            FloatingField('extended_family'),
        )

class IntakeFormPage9(forms.ModelForm):
    tobacco = forms.BooleanField(required=False, label="Do you use tobacco?")
    smoking_or_chewing_tobacco = forms.ChoiceField(required=False, widget=forms.RadioSelect, choices=[('smoking', 'Smoking'), ('chewing', 'Chewing')], label='Do you smoke or chew tobacco?')
    how_long_tobacco = forms.CharField(required=False,max_length=100, label="How long have you been using tobacco?")
    how_much_tobacco = forms.CharField(required=False,max_length=100, label="How much do you use? (packs per day, etc.)")

    alcohol = forms.BooleanField(required=False, label="Do you drink?")
    how_much_alcohol = forms.CharField(required=False,max_length=100, label="How much do you drink? (glasses per day, etc.)")
    how_often_alcohol = forms.CharField(required=False,max_length=100, label="How often do you drink?")
    what_kind_alcohol = forms.CharField(required=False,max_length=100, label="What kind of alcohol do you drink? (beer, wine, etc.)")

    marijuana = forms.BooleanField(required=False, label="Do you use marijuana or other THC-derivative products?")
    smoking_or_eating_marjuana = forms.ChoiceField(required=False, widget=forms.RadioSelect, choices=[('smoking', 'Smoking'), ('eating', 'Eating')], label='Do you smoke or eat marajuana?')
    how_much_marajuana = forms.CharField(required=False,max_length=100, label="How much do you use? (joints per day, etc.)")
    how_often_marajuana = forms.CharField(required=False,max_length=100, label="How often do you use?")
    
    soft_drinks = forms.BooleanField(required=False, label="Do you drink soft drinks regularly?")
    how_often_soft_drinks = forms.CharField(required=False,max_length=100)

    caffiene = forms.BooleanField(required=False, label="Do you drink coffee or other caffinated beverages?")
    what_form_caffiene = forms.CharField(required=False,max_length=100, label="What form of caffiene do you drink? (coffee, tea, etc.)")
    how_often_caffiene = forms.CharField(required=False,max_length=100, label="How often do you drink caffiene?")

    other_substances = forms.BooleanField(required=False, label="Do you use any other substances?")
    what_kind_other_substances = forms.CharField(required=False,max_length=100, label="What kind of substances do you use?")
    how_much_other_substances = forms.CharField(required=False,max_length=100, label="How much do you use?")
    how_often_other_substances = forms.CharField(required=False,max_length=100, label="How often do you use?")

    exercise = forms.BooleanField(required=False, label="Do you exercise on a regular basis?")
    how_often_exercise = forms.CharField(required=False,max_length=100, label="How often do you exercise?")
    what_kind_exercise = forms.CharField(required=False,max_length=100, label="What kind of exercise do you do? (running, yoga, etc.)")

    occupation = forms.BooleanField(required=False, label="Do you have an occupation currently?")
    type_occupation = forms.CharField(required=False,max_length=100, label="What kind of occupation do you have?")
    hours_per_week_occupation = forms.CharField(required=False,max_length=100, label="How many hours per week do you work?")

    class Meta:
        model = IntakeForm

        fields = [
            "tobacco",
            "smoking_or_chewing_tobacco",
            "how_long_tobacco",
            "how_much_tobacco",

            "alcohol",
            "how_much_alcohol",
            "how_often_alcohol",
            "what_kind_alcohol",

            "marijuana",
            "smoking_or_eating_marjuana",
            "how_much_marajuana",
            "how_often_marajuana",

            "soft_drinks",
            "how_often_soft_drinks",
            
            "caffiene",
            "what_form_caffiene",
            "how_often_caffiene",

            "other_substances",
            "what_kind_other_substances",
            "how_much_other_substances",
            "how_often_other_substances",

            "exercise",
            "how_often_exercise",
            "what_kind_exercise",

            "occupation",
            "type_occupation",
            "hours_per_week_occupation",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                'tobacco',
                Div(
                    Column('smoking_or_chewing_tobacco', css_class='mx-2'),
                    Column(FloatingField('how_long_tobacco'), css_class='mx-2'),
                    Column(FloatingField('how_much_tobacco'), css_class='mx-2'),
                ),
                'alcohol',
                Div(
                    Column(FloatingField('how_much_alcohol'), css_class='mx-2'),
                    Column(FloatingField('how_often_alcohol'), css_class='mx-2'),
                    Column(FloatingField('what_kind_alcohol'), css_class='mx-2'),
                ),
                'marijuana',
                Div(
                    Column('smoking_or_eating_marjuana', css_class='mx-2'),
                    Column(FloatingField('how_much_marajuana'), css_class='mx-2'),
                    Column(FloatingField('how_often_marajuana'), css_class='mx-2'),
                ),
                'soft_drinks',
                Div(
                    Column(FloatingField('how_often_soft_drinks'), css_class='mx-2'),
                ),
                'caffiene',
                Div(
                    Column(FloatingField('what_form_caffiene'), css_class='mx-2'),
                    Column(FloatingField('how_often_caffiene'), css_class='mx-2'),
                ),
                'other_substances',
                Div(
                    Column(FloatingField('what_kind_other_substances'), css_class='mx-2'),
                    Column(FloatingField('how_much_other_substances'), css_class='mx-2'),
                    Column(FloatingField('how_often_other_substances'), css_class='mx-2'),
                ),
                'exercise',
                Div(
                    Column(FloatingField('how_often_exercise'), css_class='mx-2'),
                    Column(FloatingField('what_kind_exercise'), css_class='mx-2'),
                ),
                'occupation',
                Div(
                    Column(FloatingField('type_occupation'), css_class='mx-2'),
                    Column(FloatingField('hours_per_week_occupation'), css_class='mx-2'),
                ),
            css_class='rounded-3 p-3'
            )
        )

class IntakeFormPage10(forms.ModelForm):
    pain_points = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Where do you feel pain or discomfort?")

    class Meta:
        model = IntakeForm
        fields = [
            "pain_points",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset(
                'Pain Points',
                FloatingField('pain_points'),
            css_class='rounded-3 p-3'
            )
        )

class IntakeFormPage11(forms.ModelForm):
    what_do_you_hope_to_gain_from_shiatsu = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="What are your current reasons for seeking therapy from Shrivatsa Center? Do you have a specific goal for our time together?")
    how_did_you_hear_about_us = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label="Were you referred to us? If so, by whom?")
    
    class Meta:
        model = IntakeForm
        fields = [
            "how_did_you_hear_about_us",
            "what_do_you_hope_to_gain_from_shiatsu",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'how_did_you_hear_about_us',
            'what_do_you_hope_to_gain_from_shiatsu',
        )