from django.shortcuts import render
from django.contrib import messages
from .forms import Student0, Student1, Student2,Student_Registerform,Teacher_Registrations
from .models import Student 

# Create your views here.

def index(request):
    data={}
  
    if request.method=='POST':

        us=Student.objects.get(pk=1)
        form4=Student_Registerform(request.POST,instance=us)
        # form4=Student_Registerform(request.POST)
        form4.is_valid()

        nm=form4.cleaned_data['username']
        em=form4.cleaned_data['email']
        pw=form4.cleaned_data['password']
        form4.save() #for update

        print(nm)
        print(em)
        print(pw)
        reg=Student(username=nm,email=em,password=pw) #for new object
        reg.save()
        form=Student0(request.POST)
        form1=Student1(request.POST)
        form2=Student2(request.POST)

        form.order_fields(field_order=['first_name','email','last_name'])
    else:
        form=Student0()
        form1=Student1()
        form2=Student2()
        form4=Student_Registerform()

        # form=Student(auto_id=True, label_suffix=" = " ,
        # initial={'first_name':'Mazhar','last_name':'Rasheed'},prefix="asdf")

        form.order_fields(field_order=['first_name','email','last_name'])
            
    data={'form':form ,'form1':form1,'form2':form2,'form4':form4,}
    return render(request,"student/index.html",data)

def index_teacher(request):
    data={}
    if request.method=='POST':
        form5=Teacher_Registrations(request.POST)
        # form5.is_valid()
        form5.save()
        form5=Teacher_Registrations()
        messages.add_message(request ,messages.INFO ,"Now you can log in") # both methods are working
        messages.success(request ,"Your account succesfuly created")# both methods are working generaly we use this
    else:
        form5=Teacher_Registrations()
    data={'form5':form5}
    return render(request,"student/index.html",data)