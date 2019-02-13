from django.urls import path
from . import views

urlpatterns = [
   path('', views.blog, name='blog'),
   path('post-new', views.input_post, name='post-new')
]
