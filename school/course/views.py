from django.shortcuts import redirect, render

from student.forms import Student3, Student4,Student5


def index(request):
   data={}
   try:
      if request.method=='POST':
         if request.POST.get("form_type") == 'formOne':
            print(request.POST.get("form_type"))
            form=Student3(request.POST)
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