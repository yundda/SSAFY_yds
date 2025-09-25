from django.shortcuts import render
from .models import Article
# Create your views here.
# (1) 전체 게시글 조회 후 (2) 메인 페이지 응답
def index(request):
    # (1)
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    # (2)
    return render(request, 'articles/index.html', context)