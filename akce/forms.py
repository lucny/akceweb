from django import forms

from .models import Akce


class AkceForm(forms.ModelForm):
    class Meta:
        model = Akce
        fields = ["nazev", "datum", "popis", "kategorie", "hodnoceni"]
        widgets = {
            "datum": forms.DateInput(attrs={"type": "date"}),
        }
