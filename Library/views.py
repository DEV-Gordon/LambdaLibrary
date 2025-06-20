from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Category, Posts
from django.http import FileResponse
from django.db.models import F
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
class HomeView(ListView):
    model = Posts
    template_name = 'Library/home.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Posts.objects.filter(published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = Posts.objects.filter(published=True, featured=True)[:3]
        context['categories'] = Category.objects.all()
        return context

class CategoryView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'Library/category.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Posts.objects.filter(category=self.category, published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = self.category
        return context

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Posts
    template_name = 'Library/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Posts.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['related_models'] = Posts.objects.filter(
            category=self.object.category,
            published=True
        ).exclude(id=self.object.id)[:3]
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Posts
    form_class = PostForm
    template_name = 'Library/users/post_form.html'
    success_url = reverse_lazy('Library:manage_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    form_class = PostForm
    template_name = 'Library/users/post_form.html'
    success_url = reverse_lazy('Library:manage_posts') 

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author 

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'Library/users/post_confirm_delete.html'
    success_url = reverse_lazy('Library:manage_posts') 

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author 

class UserPostsListView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'Library/users/manage_posts.html'
    context_object_name = 'user_posts'

    def get_queryset(self):
        return Posts.objects.filter(author=self.request.user).order_by('-created_at')

# Download Function
@login_required
def download_post(request, slug):
    post = get_object_or_404(Posts, slug=slug, published=True)
    
    # Count download increment
    post.downloads = F('downloads') + 1
    post.save(update_fields=['downloads'])
    post.refresh_from_db()

    # get name file 
    file_path = post.model_file.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=post.model_file.name)
    return response