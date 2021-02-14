from django import forms
from .models import Thought


class ThoughtsForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = "__all__"
        widgets = {'question': forms.TextInput(attrs={'size': 70, 'placeholder': 'What question is your deep thought about?'}), 'title': forms.TextInput(
            attrs={'size': 70, 'placeholder': 'Title'}), 'body': forms.TextInput(attrs={'size': 70, 'placeholder': 'Deep thought'})}
