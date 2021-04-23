from django import forms
from .models import MapInfoModel

class MapInfoModelAdd(forms.ModelForm):
    class Meta:
        model = MapInfoModel
        fields = ['name','genre','location','lat','lng','photo','created_at']
