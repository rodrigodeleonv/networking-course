from django import forms
from homework import models as hm


class HomeworkForm(forms.ModelForm):

    class Meta:
        model = hm.Homework
        fields = ['filename']
