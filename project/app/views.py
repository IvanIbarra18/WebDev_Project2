from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, render

from .models import (
    Advertisement,
    Celebrity,
    MovieTV,
    MovieTheater,
    News,
    NewsletterSubscription,
    Slider,
    SocialLink,
    Trailer,
    TrailerItem,
    Tweet,
)


def home(request):
    if request.method == "POST" and request.POST.get("form_type") == "signup":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        password_confirm = request.POST.get("password_confirm", "")

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Please enter a valid email address.")
            return redirect("home")

        if not username or not password or not password_confirm:
            messages.error(request, "Please complete all sign up fields.")
        elif password != password_confirm:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "That username is already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "That email is already registered.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, "Account created successfully.")
        return redirect("home")

    if request.method == "POST" and request.POST.get("form_type") == "login":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or password.")
        else:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}.")
        return redirect("home")

    if request.method == "POST" and "newsletter_email" in request.POST:
        email = request.POST.get("newsletter_email", "").strip().lower()
        if not email:
            messages.error(request, "Please enter an email for newsletter subscription.")
        else:
            _, created = NewsletterSubscription.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Thanks for subscribing to our newsletter.")
            else:
                messages.info(request, "That email is already subscribed.")
        return redirect("home")

    featured_news = News.objects.filter(section__iexact="featured").first()
    if featured_news is None:
        featured_news = News.objects.first()

    context = {
        "social_links": SocialLink.objects.all(),
        "slider_items": Slider.objects.all(),
        "theater_popular": MovieTheater.objects.filter(type__iexact="popular"),
        "theater_coming_soon": MovieTheater.objects.filter(type__iexact="coming soon"),
        "tv_popular": MovieTV.objects.filter(type__iexact="popular"),
        "tv_coming_soon": MovieTV.objects.filter(type__iexact="coming soon"),
        "sidebar_ad": Advertisement.objects.filter(section__iexact="sidebar").first(),
        "news_ad": Advertisement.objects.filter(section__iexact="news").first(),
        "celebrities": Celebrity.objects.all(),
        "trailers": Trailer.objects.all(),
        "trailer_items": TrailerItem.objects.all(),
        "featured_news": featured_news,
        "more_news_left": News.objects.filter(section__iexact="left"),
        "more_news_right": News.objects.filter(section__iexact="right"),
        "tweets": Tweet.objects.all(),
    }

    return render(request, "home.html", context)


def logout_user(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been logged out.")
    return redirect("home")
