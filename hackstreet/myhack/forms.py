# forms.py
from django import forms

class ChatForm(forms.Form):
    user_input = forms.CharField(
        label='Say something to the bot:',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type your message...'})
    )
