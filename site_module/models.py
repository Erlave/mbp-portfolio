from django.db import models

# Create your models here.
class site_model (models.Model):
    site_name = models.CharField(max_length=200,default="default-name", verbose_name='نام سایت')
    logo=models.ImageField( upload_to='logo/', height_field=None, width_field=None, max_length=None , verbose_name='لوگو سایت')
    email=models.EmailField( max_length=254 ,verbose_name='ایمیل')
    phone_number = models.CharField(("شماره تلفن"), max_length=11)
    address=models.CharField(("ادرس"), max_length=50)
    domain_name = models.CharField(("اسم دامنه"), max_length=50)

    github_link =models.URLField(("لینک گیت هاب"), max_length=200)
    instagram_link =models.URLField(("لینک اینستاگرام"), max_length=200)
    linkdin_link = models.URLField(("لینک لینکدین"), max_length=200)

    copyright_text=models.CharField(("متن کپی رایت"),default="", max_length=50)
    copy=models.CharField(("متن کپی رایت لینک"),default="", max_length=50)
    copy_url=models.URLField(("لینک کپی رایت"),default="", max_length=200)

    is_main_setting=models.BooleanField(("تنضیمات اصلی") ,default=False)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name