from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Full Name',
    }))

    email = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Email',
    }))

    message = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(attrs={
        'placeholder': 'Message (max length: 1000 characters)',
        'rows': 6,
    }))

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message')
