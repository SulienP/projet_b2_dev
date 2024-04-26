# forms.py
from django import forms
from .models import Player

class EditProfilPhoto(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['profil_photo']
        widgets = {
            'profil_photo': forms.FileInput(attrs={'accept': 'image/*'}),
        }
