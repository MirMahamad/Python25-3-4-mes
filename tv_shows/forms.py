from django import forms
from . import models


class TvShowForm(forms.ModelForm):
    class Meta:
        model = models.TVShow
        fields = '__all__'