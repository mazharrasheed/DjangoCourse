from django import forms


class Student(forms.Form):

    first_name=forms.CharField(label= "your name")
    last_name=forms.CharField(disabled=True)
    email=forms.EmailField()
    mobile=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput())
    text_area=forms.CharField(widget=forms.Textarea(attrs={'class':'somecss'}))
    checkbox=forms.CharField(widget=forms.CheckboxInput())
    fileinput=forms.CharField(widget=forms.FileInput())

class Student1(forms.Form):

    first_name=forms.CharField(error_messages={'required':"Enter Your Name "})
    last_name=forms.CharField()
    email=forms.EmailField()
    mobile=forms.IntegerField(disabled=True)
    key=forms.CharField(widget=forms.HiddenInput())

class Student2(forms.Form):

    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())




    