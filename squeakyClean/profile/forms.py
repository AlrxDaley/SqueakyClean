from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    postcode = forms.CharField(required=True)
    town_or_city = forms.CharField(required=True)
    street_address1 = forms.CharField(required=True)
    street_address2 = forms.CharField()

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "phone_number",
            "postcode",
            "town_or_city",
            "street_address1",
            "street_address2",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            return user
