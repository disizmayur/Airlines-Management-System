from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import search
# Create your views here.
def home(request):
    if request.method=="POST":
        try:
            search=get_object_or_404(search)
            return render(request,'search/result.html')
        except:
            return render(request,'search/home.html',{'eror':" Flight does not exist"})
    else:
        return render(request,'search/home.html')

def result(request):
    return render(request,'result.html')