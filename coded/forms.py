from django import forms
from coded import models


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = "__all__"

