from django import forms

from .models import ChatMessage


class MessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'chat-input',
                'placeholder': 'Сообщение...',
                'rows': 1,
            }),
        }
