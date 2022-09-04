from django.shortcuts import render, redirect
from .models import *
from .forms import PatientForm, CBCForm


def main_page(request):
    return render(request, 'records/main.html')

def createPatient(request):
    p_form = PatientForm
    if request.method == "POST":
        p_form = PatientForm(request.POST)
        if p_form.is_valid():
            p_form.save()
            return redirect('/')

    ctx = {'p_form': p_form}

    return render(request, 'records/addp.html', ctx)

def fp_page(request):
    return render(request, 'records/findp.html')

def addTests(request):
    t_form = CBCForm
    if request.method == "POST":
        t_form = CBCForm(request.POST)
        if t_form.is_valid():
            t_form.save()
            return redirect('/')

    ctx = {'t_form': t_form}

    return render(request, 'records/addt.html', ctx)

def ft_page(request):
    return render(request, 'records/findt.html')

