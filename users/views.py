from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from Library.models import Posts, Category

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'users/signup.html'

class ProfileView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'users/profile.html'
    context_object_name = 'user_posts'

    def get_queryset(self):
        # Filtrar post por el usuario
        return Posts.objects.filter(author=self.request.user).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
