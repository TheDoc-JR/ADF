from django.shortcuts import render, redirect
from .models import *
from .forms import PatientForm, CBCForm, AddTestForm, BCHForm, EnzymesForm, ShowTestForm, CreateUserForm
from django.contrib import messages
from .filters import PatientFilter, CBCFilter, BCHFilter, EnzymesFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def register_page(request):
    regform = CreateUserForm

    if request.method == "POST":
        regform = CreateUserForm(request.POST)
        if regform.is_valid():
            regform.save()
            user = regform.cleaned_data.get('username')
            messages.success(request, "Account successfully created for " + user)

            return redirect('login_page')

    ctx = {"regform": regform}
    return render(request, 'records/register.html', ctx)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, "Username or password is incorrect")

    ctx = {}
    return render(request, 'records/login.html', ctx)

def logout_user(request):
    logout(request)
    return redirect('login_page')

@login_required(login_url="login_page")
def main_page(request):
    return render(request, 'records/main.html')



class Patients:

    def __init__(self) -> None:
        pass

    @login_required(login_url="login_page")
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

    @login_required(login_url="login_page")
    def fp_page(request):
        pts = Patient.objects.all()
        pfilter = PatientFilter(request.GET, queryset=pts)
        pts = pfilter.qs
        ctx = {"pts": pts, "pfilter": pfilter}
        return render(request, 'records/findp.html', ctx)




class AddTests:

    def __init__(self) -> None:
        pass

    @login_required(login_url="login_page")
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

    @login_required(login_url="login_page")
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


    @login_required(login_url="login_page")
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

    @login_required(login_url="login_page")
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



class ShowTests:
    
    def __init__(self) -> None:
        pass

    @login_required(login_url="login_page")
    def ft_page(request):
        showt_form = ShowTestForm
        if request.method == "POST":
            showt_form = ShowTestForm(request.POST)
            showtest = request.POST.get('showtest_sel')
            
            if showt_form.is_valid():
                if showtest == "CBC":
                    return redirect('show_cbc')
                if showtest == "BCH":
                    return redirect('show_bch')
                if showtest == "Enzymes":
                    return redirect('show_enzymes')

        ctx = {'showt_form': showt_form}

        return render(request, 'records/findt.html', ctx)

    @login_required(login_url="login_page")
    def show_cbc(request):
        cbc = CBC.objects.all()
        cbc_filter = CBCFilter(request.GET, queryset=cbc)
        cbc = cbc_filter.qs
        ctx = {"cbc": cbc, "cbc_filter": cbc_filter}
        return render(request, 'records/show_cbc.html', ctx)

    @login_required(login_url="login_page")
    def show_bch(request):
        bch = BCH.objects.all()
        bch_filter = BCHFilter(request.GET, queryset=bch)
        bch = bch_filter.qs
        ctx = {"bch": bch, "bch_filter": bch_filter}
        return render(request, 'records/show_bch.html', ctx)

    @login_required(login_url="login_page")
    def show_enzymes(request):
        enzymes = Enzymes.objects.all()
        enzymes_filter = EnzymesFilter(request.GET, queryset=enzymes)
        enzymes = enzymes_filter.qs
        ctx = {"enzymes": enzymes, "enzymes_filter": enzymes_filter}
        return render(request, 'records/show_enzymes.html', ctx)

