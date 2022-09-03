from django.db import models

class Patient(models.Model):
    patient_ID = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(null=False, max_length=20)
    surname = models.CharField(null=False, max_length=20)
    bd = models.DateField()
    gender = models.CharField(max_length=6)


    def __str__(self):
        return (self.name + " " + self.surname) 



