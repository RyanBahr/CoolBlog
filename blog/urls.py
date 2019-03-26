from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('index/', views.index.as_view(), name='index'),
    path('<int:pk>', views.blogpost.as_view(), name='blogpost'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

]
