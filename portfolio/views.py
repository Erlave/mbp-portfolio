from django.shortcuts import render
from .models import portfolio,prot_title
from django.views.generic import ListView ,DetailView,TemplateView
from django.shortcuts import get_object_or_404
# Create your views here.







class portfolioListView(ListView):
    model = portfolio                  # مدلی که قراره لیست بشه
    template_name = 'port/port_page.html'  # تمپلیت برای رندر
    context_object_name = "portfolio"     # اسم متغیر داخل تمپلیت

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = prot_title.objects.filter(is_active=True).first()
        return context
    
class PortfolioDetailsView(TemplateView):
    template_name = 'port/portfolio_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailsView, self).get_context_data(**kwargs)
        slug = kwargs['slug']  # گرفتن اسلاگ از URL
        # گرفتن نمونه کار بر اساس اسلاگ و فعال بودن
        context['portfolio'] = get_object_or_404(portfolio, slug=slug, is_active=True)
        # اضافه کردن عنوان‌ها
     
        return context