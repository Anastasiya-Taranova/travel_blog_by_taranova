from django import forms
from django.forms import Form


class CityForm(Form):
    country = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "label": "Страна",
                "class": "form-control",
                "name": "country",
                "id": "country",
                "placeholder": "Введите страну",
            }
        ),
    )
    outboundpartialdate = forms.DateField(
        widget=forms.DateInput(
            format=("%Y-%m-%d"),
            attrs={"class": "outboundpartialdate", "placeholder": "Год-Месяц-День"},
        )
    )
    inboundpartialdate = forms.DateField(
        widget=forms.DateInput(
            format=("%Y-%m-%d"),
            attrs={"class": "inboundpartialdate", "placeholder": "Год-Месяц-День"},
        )
    )
    originplace = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "city",
                "id": "city",
                "placeholder": "Введите город",
            }
        ),
    )
    destinationplace = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "city",
                "id": "city",
                "placeholder": "Введите город",
            }
        ),
    )
