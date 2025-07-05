from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index),
    
    # api url patterns
    path('report', api.report),
    path('take_shot', api.store_tracking_screenshot),
    path('track', api.track),
    path('new_code', api.new_code)
]