from django.db import models


# Create your models here.
class contact_model(models.Model):
    name=models.CharField(("نام مشتری"), max_length=100)
    email=models.EmailField(("ایمیل مشتری"), max_length=254)
    massage=models.TextField(("پیام مشتری"), max_length=300)
    # created_at = models.DateTimeField(auto_now_add=True)
    is_read_admin=models.BooleanField(("خوانده شده/خوانده نشده") ,default=False)


    class Meta:
        verbose_name = 'پبام'
        verbose_name_plural = 'پبام ها'

    def __str__(self):
        return f"{self.name} - {self.email}"