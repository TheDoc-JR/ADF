import django_filters
from django_filters import CharFilter
from .models import Enzymes, Patient, CBC, BCH

class PatientFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    surname = CharFilter(field_name='surname', lookup_expr='icontains')
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['name', 'surname', 'bd']