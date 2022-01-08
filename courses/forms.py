from django import forms
from django.forms.widgets import ChoiceWidget, TextInput
from .models import Review, DataCollector
from phonenumber_field.modelfields import PhoneNumberField


gender = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"


class DataCollectorForm(forms.ModelForm):

    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control-sm",
                "placeholder": "First Name",
            }
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control-sm",
                "placeholder": "Last Name",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control-sm",
                "placeholder": "Email",
            }
        )
    )

    date_of_birth = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "class": "form-control-sm",
                "placeholder": "Birth Of Date",
                "type": "date",
            }
        ),
    )
    # gender =forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control-sm",
    #             "placeholder": "Birth Of Date",
    #             "type": "radio",
    #         }
    #     ),
       
    # )

    street_address = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={
                "class": "form-control-sm",
                "placeholder": "Address",
            }
        ),
    )

    city = forms.CharField(
        required=True,
        widget=TextInput(
            attrs={
                "class": "form-control-sm",
                "placeholder": "City",
            }
        ),
    )
    company = forms.CharField(
        required=False,
        widget=TextInput(
            attrs={
                "class": "form-control-sm",
                "placeholder": "Company",
            }
        ),
    )

    class Meta:
        model = DataCollector
        fields = "__all__"
