from django import forms
from django.contrib.auth.models import User
from secrets import compare_digest

_attrs = {
           'class':'form-control'
    }

class RegisterUserForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs=_attrs))
    email = forms.CharField(widget=forms.EmailInput(attrs=_attrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs=_attrs))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs=_attrs))

    class Meta():
        model = User
        fields = ('username','email','password')

    def clean(self):
        cleaned_data = super(RegisterUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if compare_digest(password, confirm_password):
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class LoginUserForm(forms.ModelForm):

    email = forms.CharField(widget=forms.EmailInput(attrs=_attrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs=_attrs))

    class Meta():
        model = User
        fields = ('email', 'password')


