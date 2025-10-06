from django.db import models

# Create your models here.
class work_area(models.Model):
    title=models.CharField( max_length=50 , verbose_name= "باکس مهارت")
    is_active=models.BooleanField(("فعال/ غیر فعال") , default=False)
    class Meta:
        verbose_name = 'حوزه کاری'
        verbose_name_plural = 'حوزه کاری'

    def __str__(self):
        return self.title




class home_model (models.Model):
    status = models.CharField(("وضعیت"),default='default', max_length=50)
    title_1_of_3 =models.CharField(("خط اول اسم"), max_length=50)
    title_2_of_3 =models.CharField(("خط دوم اسم"), max_length=50)
    
    descreption = models.CharField(("توضیحات"), max_length=200)


    is_active=models.BooleanField(("فعال/ غیر فعال") , default=False)

    class Meta:
        verbose_name = 'تنظیمات خانه'
        verbose_name_plural = ' تنظیمات خانه' 


    def __str__(self):
        return f"{self.title_1_of_3} {self.title_2_of_3} "
    



class services (models.Model):
    title=models.CharField(("خدمات که ارائه میدی"), max_length=50)
    projects=models.CharField(("تعداد پروژه که انجام دادی"), max_length=50)
    icon=models.CharField(("اسم به اینگلیسی برای ایکون"),null=True,blank=True,default="default-icon", max_length=50)
    icon_img=models.ImageField(("یا افضودن عکس"), upload_to="iconlogo/",null=True,blank=True, height_field=None, width_field=None, max_length=None)
    descreption=models.CharField(("توضیحات"), max_length=200)
    url=models.URLField(("لینک برای بیشتر بخوانید"),default="default-url", max_length=200)

    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)

    class Meta:
        verbose_name = 'چه خدماتی ارائه می دهم؟'
        verbose_name_plural = 'چه خدماتی ارائه می دهم؟'

    def __str__(self):
        return self.title


class my_ability(models.Model):
    title=models.CharField(("مهارتت"), max_length=50)
    icon =models.CharField(("اسم مهارت به اینگلیسی برای ایکون"),null=True,blank=True,default="default-icon", max_length=50)
    icon_img=models.ImageField(("یا افضودن عکس"), upload_to="iconlogo/",null=True,blank=True, height_field=None, width_field=None, max_length=None)
    percent=models.CharField(("درصد بلدی شما"), max_length=50)

    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)

    class Meta:
        verbose_name = ' مهارت های من '
        verbose_name_plural = ' مهارت های من  '

    def __str__(self):
        return self.title
    

class comments(models.Model):
    commet=models.CharField(("متن کامنت "), max_length=300)
    stars=models.IntegerField(("تعداد ستاره"), default=1)
    image=models.ImageField(("عکس کامنت "), upload_to='comment/', height_field=None, width_field=None, max_length=None)
    name = models.CharField(("اسم کامنت گذار"), max_length=50)
    fro=models.CharField(("مشتری کامنت گذار"), max_length=50)
    is_active=models.BooleanField(("فعال /غیر فعال") ,default=False)

    class Meta:
        verbose_name = ' کامنت'
        verbose_name_plural = ' کامنت '

    def __str__(self):
        return self.name





