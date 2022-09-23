from django.db import models


class Patient(models.Model):
    GENDER_CHOICES = [
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
    ]

    patient_ID = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(null=False, max_length=20)
    surname = models.CharField(null=False, max_length=20)
    bd = models.DateField(verbose_name="Date of birth")
    gender = models.CharField(
        null=False,
        max_length=6,
        choices=GENDER_CHOICES,
        default = "FEMALE",
    )

    def __str__(self):
        return (self.name + " " + self.surname) 


class CBC(models.Model):
    CBC_CHOICES = [
        ("RED BLOOD CELLS", "Red Blood Cells"),
        ("HEMOGLOBIN", "Hemoglobin"),
        ("HEMATOCRIT", "Hematocrit"),
    ]

    TEST_UNITS_CHOICES = [
        ("10^6/µl", "10^6/µl"),
        ("g/dL", "g/dL"),
        ("%", "%"),
    ]

    REF_VALUES_CHOICES = [
        ("(4.3 - 5.6)", "(4.3 - 5.6)"),
        ("(13.7 - 16.5)", "(13.7 - 16.5)"),
        ("(40 - 50)", "(40 - 50)"),
    ]
    
    test_name = models.CharField(null=False, max_length=80, choices=CBC_CHOICES, verbose_name="Test name", default="")
    results = models.FloatField(null=True, blank=True)
    test_units = models.CharField(null=False, max_length=200, choices=TEST_UNITS_CHOICES, verbose_name="Units", default="")
    ref = models.CharField(null=False, max_length=200, choices=REF_VALUES_CHOICES, verbose_name="Reference values", default="" )
    test_date = models.DateField(verbose_name="Test date")
    patients_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return ("COMPLETE BLOOD COUNT")

    
class BCH(models.Model):
    BCH_CHOICES = [
        ("GLUCOSE", "Glucose"),
        ("CREATININE", "Creatinine"),
        ("URIC ACID", "Uric acid"),
    ]

    TEST_UNITS_CHOICES = [
        ("mg/dL", "mg/dL"),  
    ]

    REF_VALUES_CHOICES = [
        ("(74 - 109)", "(74 - 109)"),
        ("(0.7 - 1.2)", "(0.7 - 1.2)"),
        ("(3.4 - 7.0)", "(3.4 - 7.0)"),
    ]

    test_name = models.CharField(null=False, max_length=80, choices=BCH_CHOICES, verbose_name="Test name", default="")
    results = models.FloatField(null=True, blank=True)
    test_units = models.CharField(null=False, max_length=200, choices=TEST_UNITS_CHOICES, verbose_name="Units", default="mg/dL")
    ref = models.CharField(null=False, max_length=200, choices=REF_VALUES_CHOICES, verbose_name="Reference values", default="")
    test_date = models.DateField()
    patients_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return ("BIOCHEMISTRY")


class Enzymes(models.Model):
    ENZYMES_CHOICES = [
        ("AST", "AST"),
        ("ALT", "ALT"),
        ("GAMMA-GT", "Gamma-GT"),
    ]

    TEST_UNITS_CHOICES = [
        ("UI/L", "UI/L"),  
    ]

    REF_VALUES_CHOICES = [
        ("(5-40)", "(5-40)"),
        ("(5-41)", "(5-41)"),
        ("(<60)", "(<60)"),
    ]

    test_name = models.CharField(null=False, max_length=80, choices=ENZYMES_CHOICES, verbose_name="Test name", default="")
    results = models.FloatField(null=True, blank=True)
    test_units = models.CharField(null=False, max_length=200, choices=TEST_UNITS_CHOICES, verbose_name="Units", default="UI/L")
    ref = models.CharField(null=False, max_length=200, choices=REF_VALUES_CHOICES, verbose_name="Reference values", default="")
    test_date = models.DateField()
    patients_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return ("ENZYMES")