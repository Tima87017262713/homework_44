from django.urls import path

from webapp.views.articles import add_view, detail_view
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
    path("article/", index_view,),
    path('article/add/', add_view, name='article_add'),
    path('article/<int:pk>', detail_view, name='article_detail')
]