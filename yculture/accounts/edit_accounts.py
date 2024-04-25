# forms.py
from django import forms
from .models import Player

class EditProfilPhoto(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['profil_photo']
