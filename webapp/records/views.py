from django.shortcuts import render


def main_page(request):
    return render(request, 'records/main2.html')

def addp_page(request):
    return render(request, 'records/addp.html')

