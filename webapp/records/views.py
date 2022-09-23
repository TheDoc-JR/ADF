from django.shortcuts import render, redirect
from .models import *
<<<<<<< HEAD
from .forms import PatientForm, CBCForm, AddTestForm, BCHForm, EnzymesForm
=======
from .forms import PatientForm, CBCForm, AddTestForm, BCHForm, EnzymesForm, ShowTestForm
>>>>>>> 8c3d82ebe0146043da452524fe7e089e44801561
from django.contrib import messages
from .filters import PatientFilter

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
        if cbc_form.is_valid():
            cbc_form.save()
        messages.success(request, ('RECORDS SUCCESFULLY ADDED'))
        return redirect('home')

    ctx = {'cbc_form': cbc_form}

    return render(request, 'records/add_cbc.html', ctx)

<<<<<<< HEAD
=======
def ft_page(request):
    showt_form = AddTestForm
    if request.method == "POST":
        showt_form = AddTestForm(request.POST)
        showtest = request.POST.get('showtest_sel')
        
        if showt_form.is_valid():
            return redirect('home')
            """if showtest == "CBC":
                return redirect('a_cbc')
            if showtest == "BCH":
                return redirect('a_bch')
            if showtest == "Enzymes":
                return redirect('a_enzymes')"""

    ctx = {'showt_form': showt_form}

    return render(request, 'records/findt.html', ctx)

>>>>>>> 8c3d82ebe0146043da452524fe7e089e44801561

def addBCH(request):
    bch_form = BCHForm
    if request.method == "POST":
        bch_form = BCHForm(request.POST)
        if bch_form.is_valid():
            bch_form.save()
        messages.success(request, ('RECORDS SUCCESFULLY ADDED'))
        return redirect('home')

    ctx = {'bch_form': bch_form}

    return render(request, 'records/add_bch.html', ctx)

def addEnzymes(request):
    enzymes_form = EnzymesForm
    if request.method == "POST":
        enzymes_form = EnzymesForm(request.POST)
        if enzymes_form.is_valid():
            enzymes_form.save()
        messages.success(request, ('RECORDS SUCCESFULLY ADDED'))
        return redirect('home')

    ctx = {'enzymes_form': enzymes_form}

    return render(request, 'records/add_enzymes.html', ctx)

def ft_page(request):
    cbc = CBC.objects.all()
    bch = BCH.objects.all()
    enzymes = Enzymes.objects.all()
    ctx = {"cbc": cbc, "bch": bch, "enzymes": enzymes}
    return render(request, 'records/findt.html', ctx)

