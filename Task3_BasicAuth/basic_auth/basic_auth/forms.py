from django import forms

from basic_auth.models import MyUser


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Create a password', max_length=20, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm your password', max_length=20, widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = MyUser
        fields = ['email', 'name', 'password', 'confirm_password', 'date_of_birth']
        labels = {
            'name': 'Full name',
        }
        help_texts = {
        }
        error_messages = {
            'name': {
                'max_length': 'Your name is too long.',
            },
        }

    def clean_confirm_password(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
