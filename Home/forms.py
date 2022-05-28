from tkinter import Widget
from attr import attrs
from django import forms

class SettingsForm(forms.Form):
    com_port = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-default'}))