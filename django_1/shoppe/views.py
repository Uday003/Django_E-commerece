from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'shoppe/home.html',context)
def about(request):
    return render(request,'shoppe/about.html',{'title':'E commerce'})
def electronics(request):
    return render(request,'shoppe/electronics.html')
def fashion(request):
    return render(request,'shoppe/fashion.html',)
def grocery(request):
    return render(request,'shoppe/grocery.html',)    
def successful_buy(request):
    return render(request,'shoppe/successful_buy.html',)
