from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from pages.views import *
# Create your views here.
def signn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
    return render(request, 'accounts/signin.html')
def signp(request):
    form = acctForm()
    if request.method == 'POST':
        form = acctForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(signn)
    context = {'form': form}
    return render(request, 'accounts/signup.html', context=context)

def logt(request):
    logout(request)
    return redirect(signn)
