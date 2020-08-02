from django import forms
from django.forms import ModelForm
from django.forms import TextInput

from apps.preparation.models import Skyscanner


class CityForm(ModelForm):
    class Meta:
        model = Skyscanner
        fields = ["name_city"]
        widjets = {
            "name_city": TextInput(
                attrs={
                    "class": "form-control",
                    "name": "city",
                    "id": "city",
                    "placeholder": "Введите город",
                }
            )
        }


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=["%d/%m/%Y %H:%M"])
