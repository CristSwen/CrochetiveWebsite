"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import ApparelProduct, ToysProduct, PetsProduct
from django.forms import ModelForm

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class ApparelForm(ModelForm):
    class Meta:
        model = ApparelProduct
        fields = '__all__'

class ToysForm(ModelForm):
    class Meta:
        model = ToysProduct
        fields = '__all__'

class PetsForm(ModelForm):
    class Meta:
        model = PetsProduct
        fields = '__all__'