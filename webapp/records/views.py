from django.shortcuts import render, redirect
from .models import *
from .forms import PatientForm, CBCForm, TestForm
from django.contrib import messages

def main_page(request):
    return render(request, 'records/main.html')

def createPatient(request):
    p_form = PatientForm
    if request.method == "POST":
        p_form = PatientForm(request.POST)
        if p_form.is_valid():
            p_form.save()
        messages.success(request, ('PATIENT SUCCESFULLY ADDED'))
        return redirect('home')


    ctx = {'p_form': p_form}

    return render(request, 'records/addp.html', ctx)

def fp_page(request):
    return render(request, 'records/findp.html')

def addTests(request):
    t_form = TestForm
    if request.method == "POST":
        t_form = TestForm(request.POST)
        if t_form.is_valid():
            return redirect('home')

    ctx = {'t_form': t_form}

    return render(request, 'records/addt.html', ctx)

def ft_page(request):
    return render(request, 'records/findt.html')

