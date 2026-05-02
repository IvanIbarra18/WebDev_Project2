from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):

    if request.method == "POST":
        email = request.POST.get("email")

        if email:
            Newsletter.objects.create(email=email)

    context = {
        'social_links': SocialLink.objects.all(),
        'sliders': Slider.objects.all(),

        'movies_theater_popular': MovieTheater.objects.filter(type="Popular"),
        'movies_theater_coming': MovieTheater.objects.filter(type="Coming Soon"),

        'movies_tv_popular': MovieTV.objects.filter(type="Popular"),
        'movies_tv_coming': MovieTV.objects.filter(type="Coming Soon"),

        'ads_sidebar': Advertisement.objects.filter(section="sidebar"),
        'ads_news': Advertisement.objects.filter(section="news"),

        'celebrities': Celebrity.objects.all(),
        'trailers': Trailer.objects.all(),
        'trailer_items': TrailerItem.objects.all(),

        'news': News.objects.filter(section="tabs"),
        'news_left': News.objects.filter(section="left"),
        'news_right': News.objects.filter(section="right"),

        'tweets': Tweet.objects.all(),
    }
    return render(request, 'app1/index.html', context)

def movies_view(request):

    if request.method == "POST":
        email = request.POST.get("email")

        if email:
            Newsletter.objects.create(email=email)


    return render(request, 'app1/moviesingle.html')