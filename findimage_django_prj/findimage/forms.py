from django import forms
from .models import *


class HotelForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['gallery_id', 'gallery_name', 'gallery_img' ]