from django import forms

from .models import Clip

class ClipForm(forms.ModelForm):
    class Meta:
        model = Clip
        fields = [
            'name',
            'start',
            'end'
        ]

class RawClipForm(forms.Form):
    name = forms.CharField(max_length=200)
    start = forms.IntegerField(min_value=0)
    end = forms.IntegerField(min_value=0)
