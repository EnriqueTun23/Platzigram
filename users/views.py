"""User views."""
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from .forms import ProfileForm, SignupForm

class UserDetailView(DetailView):
    """ user detail view"""
    template_name='users/detail.html',
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()


@login_required
def update_profile(request):
    """ update s user's profile view."""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website =  data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('users:update')

    else:
        form = ProfileForm()    
    return render(
    request=request,
    template_name='users/update_profile.html',
    context={
        'profile': profile,
        'user': request.user,
        'form': form
    }
    )

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
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'invalid username and password'})
    return render(request, 'users/login.html')
    

def signup(request):
    """ Sing up view. ejemplo de agregar """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    
    return render(
        request=request,
        template_name='users/signup.html',
        context={
            'form':form
        }
    )


@login_required
def logout_view(request):
    """ logout post a user."""
    logout(request)
    return redirect('users:login')