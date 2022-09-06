from django.forms import ModelForm, RadioSelect, DateInput
from django import forms
from .models import Patient, CBC
from datetime import date, datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class PatientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('home')
        self.helper.add_input(Submit('submit', 'ADD NEW PATIENT'))

        # Moving field labels into placeholders
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = False

    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'gender': RadioSelect,
            'bd': DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
        }

class TestForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('home')
        self.helper.add_input(Submit('submit', 'SELECT'))

    TEST_CHOICES = (
        ("CBC", "COMPLETE BLOOD COUNT"),
        ("BCH", "BIOCHEMISTRY"),
        ("Enzymes", "ENZYMES"),
    )

    test_sel = forms.ChoiceField(choices= TEST_CHOICES, required=True, widget=RadioSelect, label="")

class CBCForm(ModelForm):
    class Meta:
        model = CBC
        fields = '__all__' 