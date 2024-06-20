from django import forms

class Students_forms(forms.Form):
    name=forms.CharField(  max_length=30)
    age=forms.IntegerField(max_value=20)