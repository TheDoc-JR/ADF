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
        test = request.POST.get('test_sel')
        
        if t_form.is_valid():
            if test == "CBC":
                return redirect('a_cbc')

    ctx = {'t_form': t_form}

    return render(request, 'records/addt.html', ctx)

def addCBC(request):
    cbc_form = CBCForm
    if request.method == "POST":
        cbc_form = CBCForm(request.POST)
        if cbc_form.is_valid():
            cbc_form.save()
        messages.success(request, ('RECORD SUCCESFULLY ADDED'))
        return redirect('home')

    ctx = {'cbc_form': cbc_form}

    return render(request, 'records/add_cbc.html', ctx)

def ft_page(request):
    return render(request, 'records/findt.html')

