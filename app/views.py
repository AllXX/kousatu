from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Thread,Comment
from django.db.models import Q
from .forms import SearchForm,ArticleForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        #articles = Dbtest.objects.filter(text__contains=keyword)
        # articles = Thread.objects.filter(Q(text__contains=str(keyword)) | Q(text__contains=str(keyword)))
        articles = Thread.objects.filter(Q(title__contains=str(keyword)))
    else:
        searchForm = SearchForm()
        articles = Thread.objects.all()

    context = {
        'articles': articles,
        'searchForm': searchForm,
    }
    return render(request, 'app/index.html', context)

def detail(request, id):
    article = get_object_or_404(Thread, pk=id)
    
    # comment = Comment.objects.all()
    # comment = Comment.objects.select_related('title_id').get(id=id)
    comments = Comment.objects.filter(title_id=id)
    
    context = {
        'message': 'Show Article ' + str(id),
        'article': article,
        'comments':comments,
    }

    return render(request, 'app/detail.html', context)

def new(request):
    articleForm = ArticleForm()

    context = {
        'message': 'New Article',
        'articleForm': articleForm,
    }
    return render(request, 'app/new.html', context)

def new_com(request, id):
    commentForm = CommentForm()
    article = Thread.objects.get(id=id)
    
    context = {
        'message': '新規コメント',
        'commentForm': commentForm,
        'article':article,
    }
    return render(request,'app/new_com.html',context)
    
def create(request):
    articles = Thread.objects.all()
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        
        if articleForm.is_valid():
            articles = articleForm.save()
            articles.save()

    context = {
        'article':articles,
    }
    return render(request, 'app/detail.html', context)
    #本当はdetail画面に移り変わってからではなく直接indexに画面遷移をしたかった。

def create_com(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        article_id = request.POST.get("title")
        if commentForm.is_valid():
            comment= commentForm.save()

    article = get_object_or_404(Thread, pk=article_id)
    comments = Comment.objects.filter(title_id=article_id)
    context = {
        #'message': 'Create article ' + str(comment.id),
        'article': article,
        'comments': comments,
    }
    return render(request, 'app/detail.html', context)

def edit(request, id):
    return HttpResponse('this is edit ' + str(id))

def update(request, id):
    return HttpResponse('this is update ' + str(id))

def delete(request, id):
    article = get_object_or_404(Thread, pk=id)
    article.delete()

    articles = Thread.objects.all()
    context = {
        'message': 'Delete article ' + str(id),
        'articles': articles,
    }
    return render(request, 'app/index.html', context)