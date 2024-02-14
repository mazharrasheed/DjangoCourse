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

        nameval=self.cleaned_data['name']
        if len(nameval)<4:
            raise forms.ValidationError("Name should be more than 4 cheracter")

        eval=self.cleaned_data['email']
        if len(eval)<8 :
            raise forms.ValidationError("Email should be more than 8 cheracter")

        passval=self.cleaned_data['password']
        if len(passval)<8 :
            raise forms.ValidationError("Password should be more than 8 cheracter")

#Builtin Validaters try on course page

class Student4(forms.Form):

    name=forms.CharField(validators=[])
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())