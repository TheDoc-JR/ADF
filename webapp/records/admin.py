from django.contrib import admin
from records.models import Patient, CBC, BCH, Enzymes

admin.site.register(Patient)
admin.site.register(CBC)
admin.site.register(BCH)
admin.site.register(Enzymes)
