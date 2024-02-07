from django.shortcuts import render

from .forms import Student, Student1, Student2

# Create your views here.

def index(request):
    data={}
    try:
        if request.method=='POST':
            print(request.POST)
            form=Student(request.POST)
            form1=Student1(request.POST)
            form2=Student2(request.POST)
            data={'form':form}
            form.order_fields(field_order=['first_name','email','last_name'])
        else:
            form=Student()
            form1=Student1()
            form2=Student2()
            # form=Student(auto_id=True, label_suffix=" = " ,
            # initial={'first_name':'Mazhar','last_name':'Rasheed'},prefix="asdf")

            form.order_fields(field_order=['first_name','email','last_name'])
            
    except:
        pass

    data={'form':form ,'form1':form1,'form2':form2}
    return render(request,"student/index.html",data)