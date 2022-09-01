from django.shortcuts import render


def main_page(request):
    return render(request, 'records/main.html')

def addp_page(request):
    return render(request, 'records/addp.html')

def fp_page(request):
    return render(request, 'records/findp.html')

def at_page(request):
    return render(request, 'records/addt.html')

def ft_page(request):
    return render(request, 'records/findt.html')
