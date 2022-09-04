from django.shortcuts import render, redirect
from .models import *
from .forms import PatientForm


def main_page(request):
    return render(request, 'records/main.html')

def createPatient(request):
    form = PatientForm
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    ctx = {'form': form}

    return render(request, 'records/addp.html', ctx)

def fp_page(request):
    return render(request, 'records/findp.html')

def at_page(request):
    return render(request, 'records/addt.html')

def ft_page(request):
    return render(request, 'records/findt.html')

