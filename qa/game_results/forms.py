from django import forms
from .models import Game,Result

class GameForm(forms.ModelForm):
    class Meta:
        model=Game
        fields=['name']
        labels={'name':''}

class ResultForm(forms.ModelForm):
    class Meta:
        model=Result
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}