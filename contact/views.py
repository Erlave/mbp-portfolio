from django.views import View
from django.shortcuts import render, redirect
from .models import contact_model

class ContactView(View):
    template_name = 'contact/contact_page.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")  # دقیقا همون اسم فیلد HTML



        contact_model.objects.create(
            name=name,
            email=email,
            massage=massage
        )

        return redirect("home")  # بعد از ذخیره به home
