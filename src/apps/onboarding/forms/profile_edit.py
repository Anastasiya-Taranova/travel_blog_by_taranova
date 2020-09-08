from django import forms
from django.contrib.auth import get_user_model

from apps.onboarding.models import Trips
from apps.onboarding.utils.xmodels import a

User = get_user_model()


class DateInput(forms.DateInput):
    input_type = "date"


class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    name = forms.CharField(max_length=1000, required=False)

    def clean_username(self):
        cleaned = self.cleaned_data["username"]

        if not self.has_changed():
            return cleaned

        if "username" not in self.changed_data:
            return cleaned

        if User.objects.filter(username=cleaned).count():
            raise forms.ValidationError("Username has been already taken")

        return cleaned


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
