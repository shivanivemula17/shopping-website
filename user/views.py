from django.shortcuts import render
from django.http import HttpResponse
from manager . models import additem
# Create your views here.
def user(request):
    return render(request,'user/user.html')
def user_profile(request):
    return render(request,'user/user_profile.html')
def cart(request):
    return render(request,'user/cart.html')
def feedback(request):
    return render(request,'user/feedback.html')
def history(request):
    return render(request,'user/history.html')
def items_list(request):
    item1=additem.objects.all()
    return render(request,'user/items_list.html',{'item1':item1})
def order_display(request):
     return render(request,'user/order_display.html')
def tracking(request):
    return render(request,'user/tracking.html')