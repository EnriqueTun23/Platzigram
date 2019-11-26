"""User views."""
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Exception
from django.db.utils import IntegrityError

def login_view(request):
    """ Login view. """
    #pdb sirve para hacer el debugger
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'invalid username and password'})
    return render(request, 'users/login.html')
    

def signup(request):
    """ Sing up view. ejemplo de agregar """
    if request.method == 'POST':
        username = request.POST['username']
        passwd1 =  request.POST['passwd']
        passwd2 = request.POST['passwd_confirmation']

        if passwd1 != passwd2:
            return render(request, 'users/signup.html', {'error': 'password confirmation no hizo match'})
        
        try:
            user = User.objects.create_user(username=username, password=passwd1)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'El usuario ya esta registrado'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')


    return render(request, 'users/signup.html')



@login_required
def logout_view(request):
    """ logout post a user."""
    logout(request)
    return redirect('login')