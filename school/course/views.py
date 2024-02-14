from django.shortcuts import redirect, render

from student.forms import Student3 ,Student4


def index(request):
   data={}
   try:
      if request.method=='POST':
         form=Student3(request.POST)
         form1=Student4(request.POST)
         form.order_fields(field_order=['first_name','email','last_name'])
      else:
         form=Student3()
         form1=Student4()
         # form=Student(auto_id=True, label_suffix=" = " ,
         # initial={'first_name':'Mazhar','last_name':'Rasheed'},prefix="asdf")
         form.order_fields(field_order=['first_name','email','last_name'])        
   except:
      pass

   data={'form':form,'form1':form1 }
   return render(request,"course/index.html",data)