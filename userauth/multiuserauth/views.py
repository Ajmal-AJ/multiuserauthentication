from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import User,Agent,Customer


def login(request):
    if request.method == 'POST' :
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username,password=password)
        if user is not None:
            auth_login(request, user)
            if user.user_type == 'admin' :
                return redirect('multiuserauth:admin_dashboard')
            elif user.user_type == 'agent' :
                return redirect('multiuserauth:agent_dashboard')
            
            elif user.user_type == 'customers':
                return redirect('multiuserauth:customer_dashboard')
            else:
                 return redirect('multiuserauth:login')
    return render(request,'login.html')



def agent_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
       
        password = request.POST.get("password")
        first_name =  request.POST.get("firstname")
        last_name =  request.POST.get("lastname")
        usertype = request.POST.get("usertype")
        print(usertype)
        address = request.POST.get("address")
        user = User.objects.create(username=username, password=make_password(password), first_name=first_name, last_name=last_name, user_type=usertype)
        if user.user_type == 'agent' :
            Agent.objects.create(user=user, name=username, address=address)
        elif user.user_type == 'customers' :
            Customer.objects.create(user=user, name=username, address=address)
        else :
            return redirect('multiuserauth:admin_dashboard') 

        
        # Create an associated Agent instance
        return redirect('multiuserauth:admin_dashboard') 
    
    return redirect('multiuserauth:admin_dashboard') 



@login_required
def admin_dashboard(request):
    return render(request, 'administrator/adminpage.html')

@login_required
def agent_dashboard(request):
    return render(request, 'agent/agentpage.html')

@login_required
def customer_dashboard(request):
    return render(request, 'customer/customerpage.html')


def logoutuser(request):
    logout(request)
    return redirect('multiuserauth:login') 