"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class AccountForm(forms.Form):
    id_name = forms.IntegerField()
    id_password = forms.IntegerField()

