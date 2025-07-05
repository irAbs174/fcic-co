from django.db import models
from django.contrib.auth.models import User


class OrderCodes(models.Model):
    orders_number = models.CharField(unique = True, max_length=40, verbose_name='کد سفارش',null=True, blank=True )
    tracking_number = models.CharField(max_length=300, verbose_name='کد رهگیری',null=True, blank=True )
    phone_number = models.CharField(max_length=300, verbose_name='شماره تماس',null=True, blank=True )
    customer = models.CharField(max_length=300, verbose_name='مشتری',null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ بارگذاری اسکرین شات')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین به روزرسانی')
    objects = models.Manager()
    
    class Meta:
        verbose_name = 'کد رهگیری'
        verbose_name_plural = 'کد های رهگیری'
        
        
    def __str__(self):
        return f" <{self.customer}>-<{self.orders_number}> "

class RequestCustomer(models.Model):
    orders_number = models.CharField(max_length=40, verbose_name='کد سفارش',null=True, blank=True )
    customer = models.CharField(max_length=300, verbose_name='مشتری',null=True, blank=True )
    status = models.CharField(max_length=300, verbose_name='وضعیت',null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ بارگذاری اسکرین شات')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین به روزرسانی')
    objects = models.Manager()
    
    class Meta:
        verbose_name = 'مشتری درخواست دهنده'
        verbose_name_plural = 'مشتری های درخواست دهنده'
        
        
    def __str__(self):
        return f" <{self.customer}>-<{self.status}> "