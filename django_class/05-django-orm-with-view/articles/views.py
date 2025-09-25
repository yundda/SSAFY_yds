from django.shortcuts import render, redirect
from .models import Article 

# Create your views here.

# 전체 게시글 조회(1) 후 메인 페이지 응답(2)
def index(request):
    # 1. DB에 전체 게시글을 조회
    articles = Article.objects.all()

    # 2. 전체 게시글 목록을 템플릿과 함께 응답
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request,pk):
    # 1. 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # DB에 저장
    # article =Article.objects.create(title= title, content = content)
    # 위의 방법은 저장을 끊어서 유효성 검사를 할 수 없음
    article = Article(title= title, content = content)
    # 유효성 검사 후 저장 단계 필요
    article.save()
    context = {
        'title' : title,
        'content' : content
    }
    # return render(request,'articles/create.html',context)
    # 클라이언트한테 새로운 주소로 요청을 보내게끔 해야함
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/edit.html',context)

def update(request,pk):
    article = Article.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)