from django import forms
# from twango.twitteruser.models import TwitterUser


class TwangForm(forms.Form):
    # username = forms.ModelChoiceField(queryset=TwitterUser.objects.all())
    # make it yourself
    twang = forms.CharField(max_length=140, widget=forms.Textarea)
