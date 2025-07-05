from django import forms
from .tracker_models import ScreenShot

class ScreenShotForm(forms.ModelForm):
    class Meta:
        model = ScreenShot
        fields = [
            'orders_number',
            'tracking_number',
            'phone_number',
            'customer',
            'image'
            ]
