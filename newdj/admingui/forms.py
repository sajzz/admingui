from django import forms

from .models import admingui

class loginform(forms.ModelForm):
    class Meta:
        model = admingui
        fields = [
            'name',
            'ryear',
            'verified',
        ]
