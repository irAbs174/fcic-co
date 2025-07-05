from django.db import models

class ScreenShot(models.Model):
    orders_number = models.CharField(unique=True, max_length=16, verbose_name='شماره سفارش', null=True, blank=True)
    tracking_number = models.CharField(max_length=64, verbose_name='کد رهگیری', null=True, blank=True)
    phone_number = models.CharField(max_length=12, verbose_name='شماره تماس', null=True, blank=True)
    customer = models.CharField(max_length=65, verbose_name='نام کامل مشتری', blank=True)
    image = models.ImageField(upload_to='screen_shots/', verbose_name='اسکرین شات', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ بارگذاری اسکرین شات')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین به روزرسانی')
    objects = models.Manager()
    
    class Meta:
        verbose_name = 'اسکرین شات'
        verbose_name_plural = 'اسکرین شات ها'
        
    
    def __str__(self):
        return f"=> {self.tracking_number} <="
