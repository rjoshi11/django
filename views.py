from django.shortcuts import render , HttpResponse
def index(request):
     # return HttpResponse("this is homepage")
     context={
          'variable':"this is sent",
          'variable2':"this is second"
     }
     return render(request,"index.html",context)
# Create your views here.
def about(request):
     # return HttpResponse("this is about page")
     return render(request, "About.html")
def services(request):
     return render(request, "Services.html")

def contact(request):
     return render(request, "Contact.html")
