from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/
from .models import Article
from .forms import ArticleForm
# Create your views here.
def Create_View(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, 'blog/create_article.html', context)

def Detail_View(request, my_id):
    obj = get_object_or_404(Article, id = my_id)
    context = {
        'object' : obj
    }
    return render(request, 'blog/detail_article.html', context)

class ArticleListView(ListView):
    template_name = 'blog/article_list.html' # overriding
    queryset = Article.objects.all() # <blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
    template_name = 'blog/detail_article.html'
    queryset = Article.objects.all()
    # queryset = Article.objects.filter(id__gt = 1)

    def get_object(self): # urls.py 에서 <int:pk> 로 안하고 <int:id> override
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)

class ArticleCreateView(CreateView):
    template_name = 'blog/create_article.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    # success_url = '/' override get_absolute_url

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self) : 
    #     return '/'

class ArticleUpdateView(UpdateView):
    template_name = 'blog/create_article.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    # success_url = '/' override get_absolute_url

    def get_object(self): # urls.py 에서 <int:pk> 로 안하고 <int:id> override
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    queryset = Article.objects.all()
    
    # queryset = Article.objects.filter(id__gt = 1)

    def get_object(self): # urls.py 에서 <int:pk> 로 안하고 <int:id> override
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id = id_)

    def get_success_url(self):
        return reverse('blog:article-list')