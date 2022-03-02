from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class ChangeLastName(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['Last name'].label = 'Last name'

    class Meta:
        last_name = forms.CharField(
            label="Last name",
            max_length=100,
            strip=True
        )


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['username'].label = 'Login'
        self.fields['password'].label = 'Password'

    def clean(self):
        username = self.changed_data['username']
        password = self.changed_data['password']
        if not User.objects.filter(username=username).exist():
            raise forms.ValidationError(f'User {username} not found!')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Wrong password!')
        return self.changed_data
