from django.db import models

# Create your models here.
class IntakeForm(models.Model):
    # personal information
    full_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # address
    address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone_number = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=100, blank=True, null=True)

    # current care
    primary_care_provider = models.CharField(max_length=100, blank=True, null=True)
    other_care = models.TextField(blank=True, null=True)

    # questions
    takes_perscribed_medication = models.BooleanField(default=False)
    takes_herbal_medicine = models.BooleanField(default=False)
    has_done_shiatsu = models.BooleanField(default=False)
    has_cat = models.BooleanField(default=False)

    # other conditions
    allergies = models.TextField(blank=True, null=True)
    other_conditions = models.TextField(blank=True, null=True)

    # family history
    mother = models.TextField(blank=True, null=True)
    father = models.TextField(blank=True, null=True)
    maternal_grandmother = models.TextField(blank=True, null=True)
    maternal_grandfather = models.TextField(blank=True, null=True)
    paternal_grandmother = models.TextField(blank=True, null=True)
    paternal_grandfather = models.TextField(blank=True, null=True)
    sisters = models.TextField(blank=True, null=True)
    brothers = models.TextField(blank=True, null=True)
    children = models.TextField(blank=True, null=True)
    extended_family = models.TextField(blank=True, null=True)

    # lifestyle
    tobacco = models.BooleanField(default=False)
    smoking_or_chewing_tobacco = models.BooleanField(choices=[('smoking', 'Smoking'), ('chewing', 'Chewing')], blank=True, null=True)
    how_long_tobacco = models.CharField(max_length=100, blank=True, null=True)
    how_much_tobacco = models.CharField(max_length=100, blank=True, null=True)

    alcohol = models.BooleanField(default=False)
    how_much_alcohol = models.CharField(max_length=100, blank=True, null=True)
    how_often_alcohol = models.CharField(max_length=100, blank=True, null=True)
    what_kind_alcohol = models.CharField(max_length=100, blank=True, null=True)

    marijuana = models.BooleanField(default=False)
    smoking_or_eating_marjuana = models.BooleanField(choices=[('smoking', 'Smoking'), ('eating', 'Eating')], blank=True, null=True)
    how_much_marajuana = models.CharField(max_length=100, blank=True, null=True)
    how_often_marajuana = models.CharField(max_length=100, blank=True, null=True)
    
    soft_drinks = models.BooleanField(default=False)
    how_often_soft_drinks = models.CharField(max_length=100, blank=True, null=True)

    caffiene = models.BooleanField(default=False)
    what_form_caffiene = models.CharField(max_length=100, blank=True, null=True)
    how_often_caffiene = models.CharField(max_length=100, blank=True, null=True)

    exercise = models.BooleanField(default=False)
    how_often_exercise = models.CharField(max_length=100, blank=True, null=True)
    what_kind_exercise = models.CharField(max_length=100, blank=True, null=True)

    occupation = models.BooleanField(default=False)
    what_occupation = models.CharField(max_length=100, blank=True, null=True)
    hours_per_week_occupation = models.CharField(max_length=100, blank=True, null=True)

    other_substances = models.BooleanField(default=False)
    what_kind_other_substances = models.CharField(max_length=100, blank=True, null=True)
    how_much_other_substances = models.CharField(max_length=100, blank=True, null=True)
    how_often_other_substances = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 

    def __unicode__(self):
        return 

class Medication(models.Model):
    medicine = models.CharField(max_length=100, blank=True, null=True)
    dose = models.CharField(max_length=100, blank=True, null=True)
    frequency = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)

    intake_form = models.ForeignKey(IntakeForm, on_delete=models.CASCADE)

class Supplament(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    dose = models.CharField(max_length=100, blank=True, null=True)
    frequency = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)

    intake_form = models.ForeignKey(IntakeForm, on_delete=models.CASCADE)

class Condition(models.Model):
    CONDITIONS = [
        ("hypertension", "Hypertension"),
        ("diabetes", "Diabetes"),
        ("heart_attack", "Heart Attack"),
        ("stroke", "Stroke"),
        ("blood_clot", "Blood Clot"),
        ("seizures", "Seizures"),
        ("cancer", "Cancer"),
        ("mental_illness", "Mental Illness"),
    ]


    name = models.CharField(max_length=100, choices=CONDITIONS, blank=True, null=True)
    when_diagnosed = models.CharField(max_length=100, blank=True, null=True)

    intake_form = models.ForeignKey(IntakeForm, on_delete=models.CASCADE)

class Surgery(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    when = models.CharField(max_length=100, blank=True, null=True)

    intake_form = models.ForeignKey(IntakeForm, on_delete=models.CASCADE)

class Injury(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    when = models.CharField(max_length=100, blank=True, null=True)

    intake_form = models.ForeignKey(IntakeForm, on_delete=models.CASCADE)