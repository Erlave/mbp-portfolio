from django.shortcuts import render

# Create your views here.


def home_sec (request):
    return render(request,'home_page.html')




















def footer_componnent(request):
    return render(request,'footer_componnent.html')

def header_componnent(request):
    return render(request,'header_componnent.html')