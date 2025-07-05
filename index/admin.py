from .tracker_models import ScreenShot
from django.contrib import admin
from django.contrib import admin
from .report_models import (
    OrderCodes,
    RequestCustomer
    )

@admin.register(ScreenShot)
class ScreenShotAdmin(admin.ModelAdmin):
    list_display = ('orders_number', 'tracking_number', 'phone_number', 'customer', 'created_at', 'updated_at')
    search_fields = ('orders_number', 'customer', 'tracking_number')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('orders_number', 'tracking_number', 'phone_number', 'customer', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
    
    
@admin.register(OrderCodes)
class OrderCodesAdmin(admin.ModelAdmin):
    list_display = ('orders_number', 'tracking_number', 'customer', )
    search_fields = ('orders_number', 'tracking_number', 'customer', )
    list_filter = ('created_at', 'updated_at')
    
    
@admin.register(RequestCustomer)
class RequestCustomerAdmin(admin.ModelAdmin):
    list_display = ('orders_number', 'customer', 'status', )
    list_filter = ('status',)
    search_fields = ('orders_number', 'customer', 'status', )
    list_filter = ('created_at', 'updated_at')
