from django.shortcuts import render
from django.http import HttpResponse
from blog.models import post
# from blog.forms import CommentForm
from django.views import generic
from django.shortcuts import get_list_or_404, get_object_or_404, redirect


# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request): #index of blog posts
    return render(request, 'blog.html')

def bio(request):
    return render(request, 'bio.html')

def blogpost(request):
    return render("This should be a blogpost")

def sources(request):
    return render(request, 'sources.html')

class index(generic.ListView):
    context_object_name = 'index'
    model = post
    template_name = 'index.html'

class blogpost(generic.DetailView):
    model = post
    template_name = 'post_detail.html'
    paginate_by = 10

# def add_comment_to_post(request, pk):
#     commentedpost = get_object_or_404(post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = commentedpost
#             comment.save()
#             return redirect('blogpost', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'add_comment_to_post.html', {'form': form})
