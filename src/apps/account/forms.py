from django.forms import DateInput, forms

from apps.account.models import Trips


class CreateTripForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    user_location = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)
    budget = forms.IntegerField()
    participants = forms.IntegerField()
    picture = forms.ImageField()

    class Meta:
        model = Trips
        fields = "__all__"