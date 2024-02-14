from django import forms
from django.core import validators


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

# Form with Single field validaion try on student page

class Student2(forms.Form):

    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

    def clean_name(self):

        data = self.cleaned_data["name"]
        if len(data)<4:
            raise forms.ValidationError("name should be more than 4 cheracter")
            
        return data

#Full form as whole fields validaion try on course page

class Student3(forms.Form):

    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

    def clean(self) :

        cleaned_data= super().clean()
        nameval=cleaned_data['name']
        if len(nameval)<4:
            raise forms.ValidationError("Alert! Name should be more than 4 cheracter")
        eval=cleaned_data['email']
        if len(eval)<8 :
            raise forms.ValidationError("Alert! Email should be more than 8 cheracter")
        passval=cleaned_data['password']
        if len(passval)<8 :
            raise forms.ValidationError("Alert! Password should be more than 8 cheracter")

#Builtin Validaters try on course page

def start_with_m(value):
    if value[0]!="m":
        raise forms.ValidationError("Name should be starts with 'm'")

class Student4(forms.Form):

    name=forms.CharField(validators=[validators.MaxLengthValidator(10),
    validators.MinLengthValidator(5),start_with_m])
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    re_enter_password=forms.CharField(widget=forms.PasswordInput())
 
    def clean(self) :
        cleaned_data= super().clean()
        passval=cleaned_data['password']  # self.clean_data both can work
        repassval=self.cleaned_data['re_enter_password']  # clean_data both can work
        if passval!= repassval:
            raise forms.ValidationError("Enter same password in both fields")

#adding style to error massages. see in course page
class Student5(forms.Form):

    error_css_class="error"
    requried_css_class="requried"
  
    name=forms.CharField(min_length=5)
    email=forms.EmailField()
    password=forms.CharField(min_length=8, widget=forms.PasswordInput())

    