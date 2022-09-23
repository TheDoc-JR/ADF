from tkinter.tix import Select
from django.forms import ModelForm, RadioSelect, DateInput, Select
from django import forms
from .models import Enzymes, Patient, CBC, BCH
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

class AddTestForm(forms.Form):

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

    addtest_sel = forms.ChoiceField(choices= TEST_CHOICES, required=True, widget=RadioSelect, label="")

<<<<<<< HEAD
=======
class ShowTestForm(forms.Form):

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

    showtest_sel = forms.ChoiceField(choices= TEST_CHOICES, required=True, widget=RadioSelect, label="")
>>>>>>> 8c3d82ebe0146043da452524fe7e089e44801561

class CBCForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('home')
        self.helper.add_input(Submit('submit', 'ADD RECORDS'))

        # Moving field labels into placeholders
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = False

    class Meta:
        model = CBC
        fields = '__all__'
        widgets = {
            'test_name': Select,
            'test_date': DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
        } 


class BCHForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('home')
        self.helper.add_input(Submit('submit', 'ADD RECORDS'))

        # Moving field labels into placeholders
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = False

    class Meta:
        model = BCH
        fields = '__all__'
        widgets = {
            'test_name': Select,
            'test_date': DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
        } 


class EnzymesForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('home')
        self.helper.add_input(Submit('submit', 'ADD RECORDS'))

        # Moving field labels into placeholders
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = False

    class Meta:
        model = Enzymes
        fields = '__all__'
        widgets = {
            'test_name': Select,
            'test_date': DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
        }