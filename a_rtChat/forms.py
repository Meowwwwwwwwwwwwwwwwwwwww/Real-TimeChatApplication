from django.forms import ModelForm
from django import forms
from .models import GroupMessage

class ChatmessageCreateforms(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        # how a from looks = "widgets"
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'add a message', 'class': 'p-4 text-black','maxlength': '300', 'autofocus': True }),
        } 