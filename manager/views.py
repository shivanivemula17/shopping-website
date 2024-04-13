from django.shortcuts import render
from django.http import HttpResponse
from . models import additem
# Create your views here.
def manager(request):
    return render(request,'manager/manager.html')
def manager_profile(request):
    return render(request,'manager/manager_profile.html')
def add_item(request):
    if request.method == 'POST':
        itemName=request.POST['itemName']
        Description=request.POST['Description']
        cost=request.POST['cost']
        message = itemName+Description+cost
        return render(request,'manager/add_item.html',{'result':message})
    else:
        return render(request,'manager/add_item.html',{'result':"inside else"})
def customer_list(request):
    return render(request,'manager/customer_list.html')
def feedbacks(request):
    return render(request,'manager/feedbacks.html')
def historys(request):
    return render(request,'manager/historys.html')
def Item_List(request):
    item1=additem.objects.all()
    return render(request,'manager/Item_List.html',{'item1':item1})