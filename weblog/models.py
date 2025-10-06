from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته')
    is_active= models.BooleanField(default=True , verbose_name='فعال یا غیرفعال؟' ,)

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

    def __str__(self):
        return self.name
    

class Weblog(models.Model):
    name= models.CharField(max_length=100 , verbose_name='اسم')
    image1 = models.ImageField(upload_to='weblog/',null=True , blank=True , verbose_name='عکس ها' )
    image2 = models.ImageField(upload_to='weblog/',null=True , blank=True , verbose_name='عکس ها' )
    image3 = models.ImageField(upload_to='weblog/',null=True , blank=True , verbose_name='عکس ها' )
    short_description = models.CharField(max_length=300, null=True , blank=True , verbose_name='توضیحات کوتاه')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products" , null=True, blank=True , verbose_name= 'کتگوری')

    description = models.TextField(null=True , blank=True , verbose_name="توضیح کامل")

    q1=models.TextField(("سوال 1"),null=True , blank=True )
    a1=models.TextField(("جواب 1"),null=True , blank=True )
   
    q2=models.TextField(("سوال 2"),null=True , blank=True )
    a2=models.TextField(("جواب 2"),null=True , blank=True )

    q3=models.TextField(("سوال 3"),null=True , blank=True )
    a3=models.TextField(("جواب 3"),null=True , blank=True )



    creator_img=models.ImageField(("عکس سازنده "), upload_to='weblog/creators/', height_field=None, width_field=None, max_length=None)
    creator_name=models.CharField(("اسم سازتده"), max_length=50)
    creator_des=models.TextField(("توضیح سازنده"))
    slug = models.SlugField(default='' , blank=True, db_index=True, verbose_name='url عنوان در ')

    created_at = models.DateField(null=True, blank=True, auto_now_add=True)




    is_active= models.BooleanField(default=True , verbose_name='فعال یا غیرفعال؟')




    def get_absolute_url(self):
        return reverse("product_details", args=[self.slug])


    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        if not self.slug:  # اگه خالی بود
            self.slug = slugify(self.name)  # از اسم بسازه
        else:
            self.slug = slugify(self.slug)
        super(Weblog,self).save()

    class Meta:
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ'   

    def __str__(self):
        return self.name  
    

