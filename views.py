from django.contrib.auth.models import User, auth
from django.shortcuts import render,redirect
from django.contrib import messages


# Create your views here.

def register(request):

    #Handling POST Request
    if request.method == 'POST':
        name = request.POST['uname']
        passw = request.POST['upass']
        #utype = request.POST['utype']

        user = User.objects.create_user(username=name,password=passw)
        user.save()
        messages.info(request,'Registration Successful!!!')
        return redirect('login')

    #Handling GET Request
    else:
        return render(request,'register.html')

def login(request):

    # Handling POST Request
    if request.method == 'POST':
        name = request.POST['uname']
        passw = request.POST['upass']

        user = auth.authenticate(username=name,password=passw)

        if user is not None:
            auth.login(request,user)
            messages.info(request, 'Log-in Successful!!!')
            return redirect('asp')
        else:
            messages.info(request,'Invalid Credentials...')
            return redirect('login')

    #Handling GET Request
    else:
        return render(request,'login.html')

#GET Request
def asp(request):
    return render(request,'asp.html')