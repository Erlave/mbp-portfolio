from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class portfolio(models.Model):
    img=models.ImageField(("1عکس نمونه کار"), upload_to='portfolio/', height_field=None, width_field=None, max_length=None)


    title=models.CharField(("اسم"), max_length=100)
    type1=models.CharField(("با چیا پروژه رو زدی"),null=True,blank=True, max_length=100)
    type2=models.CharField(("با چیا پروژه رو زدی"),null=True,blank=True, max_length=100)
    type3=models.CharField(("با چیا پروژه رو زدی"),null=True,blank=True, max_length=100)
    type4=models.CharField(("با چیا پروژه رو زدی"),null=True,blank=True, max_length=100)




    customer=models.CharField(("مشتری"), max_length=50)
    description = models.TextField(null=True , blank=True , verbose_name="توضیح کامل")
    slug = models.SlugField(default='' , blank=True, db_index=True, verbose_name='url عنوان در ')

    url_github=models.URLField(("لینک گیت هاب پروژه"),null=True,blank=True, max_length=200)

    is_active= models.BooleanField(default=True , verbose_name='فعال یا غیرفعال؟')
    
    



    def get_absolute_url(self):
        return reverse("product_details", args=[self.slug])


    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        if not self.slug:  # اگه خالی بود
            self.slug = slugify(self.title)  # از اسم بسازه
        else:
            self.slug = slugify(self.slug)
        super(portfolio,self).save()



    class Meta:
        verbose_name = ' نمونه کار ها'
        verbose_name_plural = ' نمونه کار ها'

    def __str__(self):
        return self.title 
    







class prot_title(models.Model):
    title=models.CharField(("تایتل برای پلن ها"), max_length=100)

    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)


    class Meta:
        verbose_name = 'تایتل نمونه کار ها'
        verbose_name_plural = 'تایتل نمونه کار ها'

    def __str__(self):
        return self.title