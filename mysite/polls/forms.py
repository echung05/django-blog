from django import forms
from .models import Thought


class ThoughtsForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = "__all__"
