from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    trailer_pairs = list(zip(Trailer.objects.all(), TrailerItem.objects.all()))

    context = {
        'social_links': SocialLink.objects.all(),
        'sliders': Slider.objects.all(),
        'movies_theater': MovieTheater.objects.all(),
        'movies_tv': MovieTV.objects.all(),
        'ads': Advertisement.objects.all(),
        'celebrities': Celebrity.objects.all(),
        'trailers': Trailer.objects.all(),
        'trailer_items': TrailerItem.objects.all(),
        'trailer_pairs': trailer_pairs,
        'news': News.objects.all(),
        'tweets': Tweet.objects.all(),
    }
    return render(request, 'app1/index.html', context)

def movies_view(request):
    return render(request, 'app1/movies.html')