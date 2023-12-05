from django import forms


class ReaderDetails(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=20)
    surname = forms.CharField(label="Enter your surname", max_length=30)
    age = forms.IntegerField(label="Indicate your age", max_value=130)