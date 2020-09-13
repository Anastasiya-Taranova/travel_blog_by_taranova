from apps.account.models import Trips
from apps.onboarding.utils.xmodels import a
from django.forms import DateInput
from django.forms import forms
from suit.widgets import EnclosedInput
from suit.widgets import SuitSplitDateTimeWidget


class CreateTripForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
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
        widjets = {
            a(Trips.packing_list): EnclosedInput(prepend="$", append=".00"),
            a(Trips.start_date): SuitSplitDateTimeWidget,
        }
