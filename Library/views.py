from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Posts

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
    
class CategoryView(ListView):
    model = Posts
    template_name = 'Library/category.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Posts.objects.filter(category=self.category, published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
    
class PostDetailView(DetailView):
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