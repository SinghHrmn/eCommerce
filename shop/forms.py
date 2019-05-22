from django import forms
from .models import carttable


class ShopForm(forms.ModelForm):

    class Meta:
        model = carttable
        fields = '__all__'
