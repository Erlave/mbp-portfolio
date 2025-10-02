from .models import site_model



def site_settings(request):
    setting = site_model.objects.filter(is_main_setting=True).first()
    return {'setting': setting}




