from django.shortcuts import render
from django.http import HttpResponse
from pdfindex.models import pdf
# from blog.forms import CommentForm
from django.views import generic
from django.shortcuts import get_list_or_404, get_object_or_404, redirect

# Create your views here.
class pdflist(generic.ListView):
    context_object_name = 'pdflist'
    model = pdf
    template_name = 'pdfindex.html'

class pdfdetail(generic.DetailView):
    model = pdf
    template_name = 'pdf.html'
    paginate_by = 10


def home(request):
    return render(request, 'home.html')

def pdfindex(request):
    return render(request, 'pdfindex.html')

def pdf(request):
    return render("This should be a pdf")
