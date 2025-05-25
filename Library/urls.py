from django.urls import path
from . import views

app_name = 'Library'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('category/<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
] 