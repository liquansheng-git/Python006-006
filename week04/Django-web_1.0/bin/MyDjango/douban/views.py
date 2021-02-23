from django.shortcuts import render
from douban.models import DouBanFilmReview
from django.http import HttpResponse


# Create your views here.
def filmreview(request):
    filmreviews = DouBanFilmReview.objects.filter(doubangradestar__gt=3)
    
    return render(request, 'douban/filmreview.html', {'filmreviews':filmreviews})