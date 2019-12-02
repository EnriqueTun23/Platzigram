

# views post.
# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Models
from .models import Post
# Forms
from .forms import PostForm


@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feel.html', {'posts': posts})


@login_required
def create_post(request):
    """ create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context= {
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )