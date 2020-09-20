from django import forms
from django.forms import Form


class CityForm(Form):
    country = forms.CharField(
        error_messages={"required": ""},
        label="Введите страну",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "label": "Страна",
                "class": "form-control",
                "name": "country",
                "id": "country",
                "placeholder": "Введите страну(English)",
            }
        ),
    )
    outboundpartialdate = forms.DateField(
        error_messages={"required": ""},
        label="Дата вылета:",
        widget=forms.DateInput(
            format=("%Y-%m-%d"),
            attrs={"class": "outboundpartialdate", "placeholder": "Год-Месяц-День"},
        ),
    )
    inboundpartialdate = forms.DateField(
        error_messages={"required": ""},
        label="Дата прилета:",
        widget=forms.DateInput(
            format=("%Y-%m-%d"),
            attrs={"class": "inboundpartialdate", "placeholder": "Год-Месяц-День"},
        ),
    )
    originplace = forms.CharField(
        error_messages={"required": ""},
        label="Город вылета:",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "city",
                "id": "city",
                "placeholder": "Введите город(English)",
            }
        ),
    )
    destinationplace = forms.CharField(
        error_messages={"required": ""},
        label="Город прилета:",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "city",
                "id": "city",
                "placeholder": "Введите город(English)",
            }
        ),
    )
