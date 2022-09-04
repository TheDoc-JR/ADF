from django.forms import ModelForm
from .models import Patient, CBC

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class CBCForm(ModelForm):
    class Meta:
        model = CBC
        fields = '__all__' 