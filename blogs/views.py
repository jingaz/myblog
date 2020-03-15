from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Article

class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'latest_article_list'
    def get_queryset(self):
        """
        Return all the articles(not including those set to be published in the future).
        """
        return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
class DetailView(generic.DetailView):
    model = Article
    template_name = 'blogs/detail.html'
    def get_queryset(self):
        """
        Exclude any articles that aren't published yet.
        """
        return Article.objects.filter(pub_date__lte=timezone.now())
