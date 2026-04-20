from django import forms

from .models import Order, Review


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service_type', 'contact_info']
        widgets = {
            'contact_info': forms.TextInput(attrs={
                'placeholder': 'номер телефона / соц.сети',
                'required': 'required',
            }),
        }


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'reting']
