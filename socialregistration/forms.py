"""
Created on 22.09.2009

@author: alen
"""
from django import forms
from django.utils.translation import gettext as _

from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.RegexField(r'\w+', max_length=255)
    email = forms.EmailField(required=False)

    def __init__(self, user, profile, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.user = user
        self.profile = profile

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.all().filter('username =', username).get()

        if user:
            raise forms.ValidationError(_('This username is already in use.'))
        else:
            return username

    def save(self):
        self.user.username = self.cleaned_data.get('username')
        self.user.email = self.cleaned_data.get('email')
        self.user.save()
        self.profile.user = self.user
        self.profile.save()
        return self.user