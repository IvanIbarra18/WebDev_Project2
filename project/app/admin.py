from django.contrib import admin

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


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("movie_title", "movie_genre", "lower_rating", "upper_rating")
    search_fields = ("movie_title", "movie_genre")


@admin.register(MovieTheater)
class MovieTheaterAdmin(admin.ModelAdmin):
    list_display = ("movie_title", "type", "movie_genre", "lower_rating", "upper_rating")
    list_filter = ("type",)
    search_fields = ("movie_title", "movie_genre")


@admin.register(MovieTV)
class MovieTVAdmin(admin.ModelAdmin):
    list_display = ("movie_title", "type", "movie_genre", "lower_rating", "upper_rating")
    list_filter = ("type",)
    search_fields = ("movie_title", "movie_genre")


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("section", "img_src", "img_width", "img_height")
    list_filter = ("section",)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "icon_class", "url")


@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = ("trailer_url",)


@admin.register(TrailerItem)
class TrailerItemAdmin(admin.ModelAdmin):
    list_display = ("description", "duration", "img_src")


@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display = ("celebrity_name", "celebrity_type", "celebrity_url")
    search_fields = ("celebrity_name", "celebrity_type")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "time")
    list_filter = ("section",)
    search_fields = ("title", "content")


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("short_content",)

    @staticmethod
    def short_content(obj):
        return obj.content[:80]


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)
