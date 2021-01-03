from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'state', 'country')

    def save(self, commit=True):
        user = super(ProfileRegisterForm, self).save(commit=False)
        user.city = self.cleaned_data['city']
        user.state = self.cleaned_data['state']
        user.country = self.cleaned_data['country']

        if commit:
            user.save()

        return user
    