from django import forms
from .models import Zone


class ZoneForm(forms.ModelForm):

    class Meta:

        model = Zone

        fields = ['zone_name']

        widgets = {

            'zone_name': forms.TextInput(
                attrs={'class': 'form-control'}
            )

        }