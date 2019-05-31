from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    # def log_me_in(self):
    #     username = self.cleaned_data.get("username", "")
    #     password = self.cleaned_data.get("password", "")
