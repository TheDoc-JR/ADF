from django.shortcuts import render, redirect
from .models import *
from .forms import PatientForm, CBCForm, AddTestForm, BCHForm, EnzymesForm
from django.contrib import messages
from .filters import PatientFilter

def main_page(request):
    return render(request, 'records/main.html')

def createPatient(request):
    p_form = PatientForm
    if request.method == "POST":
        p_form = PatientForm(request.POST)
        try:
            p_form.save()
            messages.success(request, ('PATIENT SUCCESFULLY ADDED'))
        except OverflowError: 
            messages.error(request, ('IT HAS BEEN AN ERROR ADDING THIS PATIENT'))
            return redirect('home')
        
        return redirect('home')

    ctx = {'p_form': p_form}

    return render(request, 'records/addp.html', ctx)

def fp_page(request):
    pts = Patient.objects.all()
    pfilter = PatientFilter(request.GET, queryset=pts)
    pts = pfilter.qs
    ctx = {"pts": pts, "pfilter": pfilter}
    return render(request, 'records/findp.html', ctx)

def addTests(request):
    t_form = AddTestForm
    if request.method == "POST":
        t_form = AddTestForm(request.POST)
        test = request.POST.get('addtest_sel')
        
        if t_form.is_valid():
            if test == "CBC":
                return redirect('a_cbc')
            if test == "BCH":
                return redirect('a_bch')
            if test == "Enzymes":
                return redirect('a_enzymes')

    ctx = {'t_form': t_form}

    return render(request, 'records/addt.html', ctx)

def addCBC(request):
    cbc_form = CBCForm
    if request.method == "POST":
        cbc_form = CBCForm(request.POST)
        try:
            cbc_form.save()
            messages.success(request, ('RECORDS SUCCESFULLY ADDED'))
        except:
            messages.error(request, ('IT HAS BEEN AN ERROR ADDING THIS RECORDS'))
            return redirect('home')
        return redirect('home')

    ctx = {'cbc_form': cbc_form}

    return render(request, 'records/add_cbc.html', ctx)


def addBCH(request):
    bch_form = BCHForm
    if request.method == "POST":
        bch_form = BCHForm(request.POST)
        try:
            bch_form.save()
            messages.success(request, ('RECORDS SUCCESFULLY ADDED'))
        except:
            messages.error(request, ('IT HAS BEEN AN ERROR ADDING THIS RECORDS'))
            return redirect('home')
        return redirect('home')
    

    ctx = {'bch_form': bch_form}

    return render(request, 'records/add_bch.html', ctx)

def addEnzymes(request):
    enzymes_form = EnzymesForm
    if request.method == "POST":
        enzymes_form = EnzymesForm(request.POST)
        try:
            enzymes_form.save()
            messages.success(request, ('RECORDS SUCCESFULLY ADDED'))
        except:
            messages.error(request, ('IT HAS BEEN AN ERROR ADDING THIS RECORDS'))
            return redirect('home')
        return redirect('home')

    ctx = {'enzymes_form': enzymes_form}

    return render(request, 'records/add_enzymes.html', ctx)

def ft_page(request):
    cbc = CBC.objects.all()
    bch = BCH.objects.all()
    enzymes = Enzymes.objects.all()
    """tfilter = TestsFilter(request.GET, queryset=enzymes)
    cbc = tfilter.qs
    bch = tfilter.qs
    enzymes = tfilter.qs"""
    ctx = {"cbc": cbc, "bch": bch, "enzymes": enzymes}
    return render(request, 'records/findt.html', ctx)

