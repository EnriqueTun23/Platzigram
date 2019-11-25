"""User views."""
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


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
    return render(request, 'users/signup.html')



@login_required
def logout_view(request):
    """ logout post a user."""
    logout(request)
    return redirect('login')