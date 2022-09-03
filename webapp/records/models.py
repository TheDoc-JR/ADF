from django.db import models

class Patient(models.Model):
    patient_ID = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(null=False, max_length=20)
    surname = models.CharField(null=False, max_length=20)
    bd = models.DateField()
    gender = models.CharField(max_length=6)

    def __str__(self):
        return (self.name + " " + self.surname) 


class CBC(models.Model):
    test_name = models.CharField(null=False, max_length=80)
    results = models.FloatField(null=True, blank=True)
    test_units = models.CharField(null=False, max_length=210)
    ref = models.CharField(null=False, max_length=200, verbose_name="ref. values")
    test_date = models.DateField()
    patients_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return ("COMPLETE BLOOD COUNT")

