from django.shortcuts import render

# Create your views here.

def portfolio (request):
    return render(request,'port/port_page.html')