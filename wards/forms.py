from django import forms
from .models import Ward


class WardForm(forms.ModelForm):

    class Meta:

        model = Ward

        fields = [
            'ward_name',
            'zone'
        ]

        widgets = {

            'ward_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'zone': forms.Select(
                attrs={'class': 'form-select'}
            ),

        }