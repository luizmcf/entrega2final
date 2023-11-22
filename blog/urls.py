from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:category_slug>/<slug:slug>', views.detail, name='post_detail'),
    path('<slug:slug>', views.category, name='category_detail'),
]