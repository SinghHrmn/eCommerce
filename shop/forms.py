from django import forms
from .models import CartTable


class ShopForm(forms.ModelForm):

    class Meta:
        model = CartTable
        fields = '__all__'
