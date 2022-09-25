from tkinter.tix import Select
from django.forms import ModelForm, RadioSelect, DateInput, Select
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Enzymes, Patient, CBC, BCH
from datetime import date, datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class CreateUserForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('home')
        self.helper.add_input(Submit('submit', 'Register'))

        # Moving field labels into placeholders
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = False

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

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


class CBCForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('home')
        self.helper.add_input(Submit('submit', 'ADD RECORDS'))
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-5'
        helper.field_class = 'col-lg-5'

        # Moving field labels into placeholders
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = True

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
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-5'
        helper.field_class = 'col-lg-5'

        # Moving field labels into placeholders
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = True

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
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-5'
        helper.field_class = 'col-lg-5'

        # Moving field labels into placeholders
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = True

    class Meta:
        model = Enzymes
        fields = '__all__'
        widgets = {
            'test_name': Select,
            'test_date': DateInput(attrs={'type': 'date', 'max': datetime.now().date()}),
        }

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