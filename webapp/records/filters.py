import django_filters
from django_filters import CharFilter
from .models import Patient, CBC, BCH, Enzymes

class PatientFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    surname = CharFilter(field_name='surname', lookup_expr='icontains')

    class Meta:
        model = Patient
        fields = ['patient_ID', 'gender']

class CBCFilter(django_filters.FilterSet):
    
    class Meta:
        model = CBC
        fields = ['test_name', 'test_date', 'patients_ID']
        
class BCHFilter(django_filters.FilterSet):
    
    class Meta:
        model = BCH
        fields = ['test_name', 'test_date', 'patients_ID']

class EnzymesFilter(django_filters.FilterSet):
    
    class Meta:
        model = Enzymes
        fields = ['test_name', 'test_date', 'patients_ID']
        