from django.shortcuts import render,redirect
from django.contrib import messages
from app19.models import ProductModel
from django.core.paginator import Paginator


def DisplayIndex(request):
    return render(request,'Index.html')


def DisplayAdmin_Login(request):
    return render(request,'Admin_Login.html')


def DisplayAdmin_Login_checked(request):
    un = request.POST.get("n1")
    pa = request.POST.get("n2")
    if un == "kunu" and pa == "kunu":
        return redirect('Admin_home')
    else:
        messages.error(request,'Invalid User')
        return redirect('Admin_Login')


def DisplayAdmin_home(request):
    return render(request,'Admin_home.html')


def DisplayAdmin_View_User(request):
    return render(request,'Admin_View_User.html')


def DisplayAdmin_View_Product(request):
    #result = ProductModel.objects.all()
    #return render(request,'Admin_View_Product.html',{"data":result})

     result = ProductModel.objects.all()
     pa = Paginator(result,3)
     page_number = request.GET.get("page_no",2)
     page = pa.page(page_number)
     return render(request,'Admin_View_Product.html',{"page":page})

def DisplaySave_Product(request):
    na = request.POST.get('t1')
    pr = request.POST.get('t2')
    qnt = request.POST.get('t3')
    img = request.FILES['t4']
    status = 'active'
    ProductModel(name=na,price=pr,quantity=qnt,photo=img,status=status).save()
    return redirect('Admin_View_Product')


def DisplayAdd_To_Cart(request):
    k = request.GET.get('c1')
    v = request.GET.get('c2')
    response = redirect('In_Cart')
    response.set_cookie(k,v)
    return response


def DisplayIn_Cart(request):
    return render(request,'In_Cart.html',{'Data':request.COOKIES})
