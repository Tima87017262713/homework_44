from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Article


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'article_create.html')
    article_data = {
        'title': request.POST.get('title'),
        'text': request.POST.get('text'),
        'author': request.POST.get('author'),
    }
    article = Article.objects.create(**article_data)
    return redirect('article_detail', pk=article.pk)


def detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', context={
        'article': article
    })

# 2-й вариант
# def detail_view(request, pk):
#     ## article_pk = request.GET.get('pk')
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponseNotFound("Not Found")
#     return render(request, 'article.html', context={
#         'article': article
#     })
