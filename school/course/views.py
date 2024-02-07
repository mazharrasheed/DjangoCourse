from django.shortcuts import render

# Create your views here.
def index(request):
   
   print("im course view")
   return render(request,"course/index.html")