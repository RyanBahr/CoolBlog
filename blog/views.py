from django.shortcuts import render
from django.http import HttpResponse
from blog.models import post
from django.views import generic

# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request): #index of blog posts
    return render(request, 'blog.html')

def bio(request):
    return render(request, 'bio.html')

def blogpost(request):
    return render("This should be a blogpost")

class index(generic.ListView):
    context_object_name = 'index'
    model = post
    template_name = 'index.html'

class blogpost(generic.DetailView):
    model = post
    template_name = 'post_detail.html'
    paginate_by = 10
