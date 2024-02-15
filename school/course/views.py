from django.shortcuts import redirect, render

from student.forms import Student3, Student4, Student5

from .models import users


def index(request):
   data={}
   try:
      if request.method=='POST':
         if request.POST.get("form_type") == 'formOne':
            
            form=Student3(request.POST)
            form.is_valid()
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']
            pw=form.cleaned_data['password']

            # reg=users(username=nm,email=em,password=pw) create user
            # reg=users(id=1,username=nm,email=em,password=pw) update user
            # reg.save()
         
            reg=users(id=1)
            reg.delete()
            print("i m here")
            form4=Student4()
            form5=Student5()
         elif request.POST.get("form_type") == 'formTwo':
            form=Student3()
            form4=Student4(request.POST)
            form5=Student5()
         else:
            form=Student3()
            form4=Student4()
            form5=Student5(request.POST)
      else:
         form=Student3()
         form4=Student4()
         form5=Student5()
         # form=Student(auto_id=True, label_suffix=" = " ,
         # initial={'first_name':'Mazhar','last_name':'Rasheed'},prefix="asdf")
         form.order_fields(field_order=['name','email'])        
   except:
      pass

   data={'form':form,'form4':form4 ,'form5':form5}
   return render(request,"course/index.html",data)

def show_details(request,cou):

   if cou==1:
      course=f"({cou}) Primery"
   if cou==2:
      course=f"({cou}) Secondary"
   if cou==3:
      course=f"({cou}) Metric"

   data={'yr':course}

   return render(request,'course/details.html',data)