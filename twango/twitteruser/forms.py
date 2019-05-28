from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    display_name = forms.CharField(max_length=100)
    # bio = forms.CharField(widget=forms.Textarea(attrs={"rows": "3"}))
    password = forms.CharField(widget=forms.PasswordInput())
    # email = forms.EmailField()
