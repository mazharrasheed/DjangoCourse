from django import forms


class Student(forms.Form):

    first_name=forms.CharField(label= "your name")
    last_name=forms.CharField(disabled=True)
    email=forms.EmailField()
    mobile=forms.IntegerField()

class Student1(forms.Form):

    first_name=forms.CharField(error_messages={'required':"Enter Your Name "})
    last_name=forms.CharField()
    email=forms.EmailField()
    mobile=forms.IntegerField(disabled=True)
    key=forms.CharField(widget=forms.HiddenInput())

    