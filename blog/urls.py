from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('index/', views.index.as_view(), name='index'),
    path('<int:pk>', views.blogpost.as_view(), name='blogpost'),
    # path('pdfindex/', views.pdfindex.as_view(), name='pdfindex'),
    # path('<int:pk>', views.pdf.as_view(), name='pdf'),

    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
