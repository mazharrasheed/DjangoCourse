from django.shortcuts import render


# Create your views here.
def index(request):

    print("i m fee view")
    return render(request,"fee/index.html")