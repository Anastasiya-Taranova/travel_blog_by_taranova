from apps.account.models import Trips
from django.forms import forms


class CreateTripForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "name",
                "name": "name",
                "id": "name",
                "placeholder": "Введите имя",
            }
        ),
    )
    user_location = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
    start_date = forms.DateField()
    end_date = forms.DateField()
    budget = forms.IntegerField()
    participants = forms.IntegerField()
    picture = forms.ImageField()

    class Meta:
        model = Trips
        fields = "__all__"
