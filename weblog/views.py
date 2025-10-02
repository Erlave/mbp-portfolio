from django.shortcuts import render

# Create your views here.
def weblog (request):
    return render(request,'weblog/weblog_page.html')