from django.urls import path

from . import views as pdf_views

urlpatterns = [
    path('', pdf_views.pdflist.as_view(), name='pdflist'),
    # path('pdfindex/', pdf_views.pdfindex(), name='pdfindex'),
    path('<int:pk>', pdf_views.pdfdetail.as_view(), name='pdfdetail'),

    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
