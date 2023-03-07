from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIPClient, "VIPClient"),
    (CLIENT, "CLIENT")
)

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (OTHER, "OTHER")
)

KYRGYZSTAN = 1
RUSSIA = 2
KAZAKHSTAN = 3

COUNTRY_TYPE = (
    (KYRGYZSTAN, "KYRGYZSTAN"),
    (RUSSIA, "RUSSIA"),
    (KAZAKHSTAN, "KAZAKHSTAN")
)

YES = 1
NO = 2

GAME_TYPE = (
    (YES, "YES"),
    (NO, "NO")
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    country = forms.ChoiceField(choices=COUNTRY_TYPE, required=True)
    region = forms.IntegerField(required=True)
    height = forms.IntegerField(required=True)
    weight = forms.IntegerField(required=True)
    game = forms.ChoiceField(choices=GAME_TYPE, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "user_type",
            "gender",
            "country",
            "region",
            "height",
            "weight",
            "game"
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

#######################################################################

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        username = UsernameField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ваш логин',
            'id': 'hello'
        }))

        password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    'class': "form_control",
                    'placeholder': 'password',
                    'id': 'hi'
                }
            )
        )

