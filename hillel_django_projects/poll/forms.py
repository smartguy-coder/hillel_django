from django import forms
from .models import *


class NewQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'opened']


class NewChoice(forms.Form):
    question = forms.ModelChoiceField(queryset=Question.objects.all(), label='Question to answer', empty_label="CHOOSE THE QUESTION")
    choice_text = forms.CharField(max_length=200, empty_value=False)

