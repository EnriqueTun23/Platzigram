

# views post.
# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
# Models
from .models import Post
# Forms
from .forms import PostForm

class PostFeedView(LoginRequiredMixin, ListView):
    """ Return all published posts."""
    template_name = "posts/feel.html"
    model = Post
    ordering = ('-created',)
    paginate_by = 20
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """ return post detail"""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """ create new posts """
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """ add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] =  self.request.user
        context['profile'] = self.request.user.profile
        return context



# @login_required
# def create_post(request):
#     """ create new post view."""
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
#     else:
#         form = PostForm()

#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context= {
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile
#         }
#     )