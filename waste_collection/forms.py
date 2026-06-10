from django import forms
from .models import WasteCollection


class WasteCollectionForm(forms.ModelForm):

    class Meta:
        model = WasteCollection

        fields = [
            'collection_date',
            'collection_time',
            'ward',
            'vehicle',
            'loaded_weight',
            'empty_weight',
        ]

        widgets = {
            'collection_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),

            'collection_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),

            'ward': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'vehicle': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'loaded_weight': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'empty_weight': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
        }