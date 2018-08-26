from django import forms

from .models import Clip

class ClipForm(forms.ModelForm):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"placeholder": "Name",}))
    start = forms.IntegerField(min_value=0, initial=0)
    end = forms.IntegerField(min_value=0, initial=0)
    class Meta:
        model = Clip
        fields = [
            'name',
            'start',
            'end'
        ]

    def clean_end(self):
        end = self.cleaned_data.get("end")
        start = self.cleaned_data.get("start")
        if end > start:
            return end
        else:
            raise forms.ValidationError("The end of the clip can't be before the start")
