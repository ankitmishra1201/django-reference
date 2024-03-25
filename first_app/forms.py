from django import forms

class FormName(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea, max_length=1000)
                    