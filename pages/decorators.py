from django.shortcuts import render,redirect

def check(func):
    def inner(request):
        if request.user.is_authenticated:
           return func(request)
        else:
           return redirect('signin')
    return inner