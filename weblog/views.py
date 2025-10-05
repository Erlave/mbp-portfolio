from django.shortcuts import render
from .models import Weblog,Category
from django.views.generic import ListView ,DetailView,TemplateView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta


# Create your views here.
def weblog (request):
    return render(request,'weblog/weblog_page.html')




class WeblogListView(ListView):
    model = Weblog
    template_name = 'weblog/weblog_page.html'
    context_object_name = "weblogs"


    def get_queryset(self):
        base = super().get_queryset()
        data = base.filter(is_active=True)

        # فیلتر بر اساس دسته‌بندی
        category_id = self.request.GET.get("category")
        if category_id:
            data = data.filter(category_id=category_id)

        # فیلتر بر اساس سرچ
        query = self.request.GET.get("q")
        if query:
            data = data.filter(name__icontains=query)  # سرچ در نام محصول
            # می‌تونی توضیحات یا برند هم اضافه کنی
            # data = data.filter(Q(nameicontains=query) | Q(descriptionicontains=query))
        
        
        return data





    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)
        context['selected_category'] = self.request.GET.get("category")
        context['search_query'] = self.request.GET.get("q", "")
        weekago = timezone.now() - timedelta(days = 7)
        newest = Weblog.objects.filter(is_active=True , created_at__gte =weekago)
        context['newest'] = newest

        return context
        
    


class weblogDetailsView(TemplateView):
    template_name = 'weblog/weblog_details.html'

    def get_context_data(self, **kwargs):
        context = super(weblogDetailsView, self).get_context_data(**kwargs)
        slug = kwargs['slug']  # گرفتن اسلاگ از URL
        # گرفتن نمونه کار بر اساس اسلاگ و فعال بودن
        context['w'] = get_object_or_404(Weblog, slug=slug, is_active=True)
        # اضافه کردن عنوان‌ها
     
        return context
    
