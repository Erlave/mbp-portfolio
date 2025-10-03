from django.shortcuts import render
from .models import services ,work_area,home_model,my_ability,comments
# Create your views here.


def home_sec (request):
    work=work_area.objects.filter(is_active=True)
    home=home_model.objects.filter(is_active=True).first()
    serv=services.objects.filter(is_active=True)
    ability=my_ability.objects.filter(is_active=True)
    com=comments.objects.filter(is_active=True)




    context={'work':work,
            'home':home,
            'serv':serv,
            'ability':ability,
            'com':com,

             }


    return render(request,'page.html',context)










def sec3(request):
    ability=my_ability.objects.filter(is_active=True)


    context={

             }

    return render(request ,'homes/sec3.html',context)











def footer_componnent(request):
    return render(request,'footer_componnent.html')

def header_componnent(request):
    return render(request,'header_componnent.html')