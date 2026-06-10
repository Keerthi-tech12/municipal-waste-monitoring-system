from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):

    class Meta:

        model = Vehicle

        fields = [
            'vehicle_number',
            'vehicle_type',
            'capacity_kg',
            'status'
        ]

        widgets = {

            'vehicle_number': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'vehicle_type': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'capacity_kg': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'status': forms.Select(
                attrs={'class': 'form-select'}
            ),

        }