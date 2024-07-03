from django import forms

from .models import Developer


class DeveloperForm(forms.ModelForm):

    class Meta:
        model = Developer
        fields = ['first_name', 'last_name', 'user_name']
