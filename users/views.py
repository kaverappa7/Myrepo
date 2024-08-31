from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request,'dashboard.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
            return render(request,'user/signup.html',{'form':form})
        


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')#redirect to the dashboard or another page
    else:
        form = AuthenticationForm()
        return render(request,'user/login.html',{'form':form}) 
    

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')