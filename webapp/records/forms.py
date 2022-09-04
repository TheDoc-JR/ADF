from django.forms import ModelForm, RadioSelect, DateInput
from .models import Patient, CBC
from datetime import date, datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PatientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('home')
        self.helper.add_input(Submit('submit', 'ADD NEW PATIENT'))

    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'gender': RadioSelect,
            'bd': DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
        }

class CBCForm(ModelForm):
    class Meta:
        model = CBC
        fields = '__all__' 