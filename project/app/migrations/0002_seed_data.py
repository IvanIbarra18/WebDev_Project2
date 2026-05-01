from django.db import migrations


def seed_data(apps, schema_editor):
    Slider = apps.get_model("app", "Slider")
    Advertisement = apps.get_model("app", "Advertisement")
    SocialLink = apps.get_model("app", "SocialLink")
    Trailer = apps.get_model("app", "Trailer")
    TrailerItem = apps.get_model("app", "TrailerItem")
    Celebrity = apps.get_model("app", "Celebrity")
    News = apps.get_model("app", "News")
    Tweet = apps.get_model("app", "Tweet")
    MovieTheater = apps.get_model("app", "MovieTheater")
    MovieTV = apps.get_model("app", "MovieTV")

    if not SocialLink.objects.exists():
        SocialLink.objects.bulk_create(
            [
                SocialLink(name="Facebook", anchor_class="", icon_class="ion-social-facebook", url="#"),
                SocialLink(name="Twitter", anchor_class="", icon_class="ion-social-twitter", url="#"),
                SocialLink(name="Google+", anchor_class="", icon_class="ion-social-googleplus", url="#"),
                SocialLink(name="YouTube", anchor_class="", icon_class="ion-social-youtube", url="#"),
            ]
        )

    if not Slider.objects.exists():
        Slider.objects.bulk_create(
            [
                Slider(
                    image_src="images/uploads/slider1.jpg",
                    image_width=285,
                    image_height=437,
                    anchor_url="#",
                    movie_genre="Sci-fi",
                    movie_title="Interstellar",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                Slider(
                    image_src="images/uploads/slider2.jpg",
                    image_width=285,
                    image_height=437,
                    anchor_url="#",
                    movie_genre="Action",
                    movie_title="The Revenant",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                Slider(
                    image_src="images/uploads/slider3.jpg",
                    image_width=285,
                    image_height=437,
                    anchor_url="#",
                    movie_genre="Comedy",
                    movie_title="Die Hard",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                Slider(
                    image_src="images/uploads/slider4.jpg",
                    image_width=285,
                    image_height=437,
                    anchor_url="#",
                    movie_genre="Sci-fi",
                    movie_title="The Walk",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
            ]
        )

    if not MovieTheater.objects.exists():
        MovieTheater.objects.bulk_create(
            [
                MovieTheater(
                    type="popular",
                    img_src="images/uploads/mv-item1.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Sci-fi",
                    movie_title="Interstellar",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTheater(
                    type="popular",
                    img_src="images/uploads/mv-item2.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Action",
                    movie_title="The Revenant",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTheater(
                    type="popular",
                    img_src="images/uploads/mv-item3.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Comedy",
                    movie_title="Die Hard",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTheater(
                    type="popular",
                    img_src="images/uploads/mv-item4.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Sci-fi",
                    movie_title="The Walk",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTheater(
                    type="coming soon",
                    img_src="images/uploads/mv-item5.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Sci-fi",
                    movie_title="Interstellar",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTheater(
                    type="coming soon",
                    img_src="images/uploads/mv-item6.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Action",
                    movie_title="The Revenant",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTheater(
                    type="coming soon",
                    img_src="images/uploads/mv-item7.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Comedy",
                    movie_title="Die Hard",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTheater(
                    type="coming soon",
                    img_src="images/uploads/mv-item8.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Sci-fi",
                    movie_title="The Walk",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
            ]
        )

    if not MovieTV.objects.exists():
        MovieTV.objects.bulk_create(
            [
                MovieTV(
                    type="popular",
                    img_src="images/uploads/mv-item1.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Sci-fi",
                    movie_title="Interstellar",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTV(
                    type="popular",
                    img_src="images/uploads/mv-item2.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Action",
                    movie_title="The Revenant",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTV(
                    type="popular",
                    img_src="images/uploads/mv-item3.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Comedy",
                    movie_title="Die Hard",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTV(
                    type="popular",
                    img_src="images/uploads/mv-item4.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Sci-fi",
                    movie_title="The Walk",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTV(
                    type="coming soon",
                    img_src="images/uploads/mv-item5.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Sci-fi",
                    movie_title="Interstellar",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTV(
                    type="coming soon",
                    img_src="images/uploads/mv-item6.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Action",
                    movie_title="The Revenant",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTV(
                    type="coming soon",
                    img_src="images/uploads/mv-item7.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Comedy",
                    movie_title="Die Hard",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
                MovieTV(
                    type="coming soon",
                    img_src="images/uploads/mv-item8.jpg",
                    img_width=185,
                    img_height=284,
                    anchor_url="#",
                    movie_genre="Sci-fi",
                    movie_title="The Walk",
                    lower_rating="7.4",
                    upper_rating="10",
                ),
            ]
        )

    if not Advertisement.objects.exists():
        Advertisement.objects.bulk_create(
            [
                Advertisement(section="sidebar", img_src="images/uploads/ads1.png", img_width=336, img_height=296),
                Advertisement(section="news", img_src="images/uploads/ads2.png", img_width=728, img_height=106),
            ]
        )

    if not Celebrity.objects.exists():
        Celebrity.objects.bulk_create(
            [
                Celebrity(
                    anchor_url="#",
                    img_width=70,
                    img_height=70,
                    celebrity_url="images/uploads/ava1.jpg",
                    celebrity_name="Samuel N. Jack",
                    celebrity_type="Actor",
                ),
                Celebrity(
                    anchor_url="#",
                    img_width=70,
                    img_height=70,
                    celebrity_url="images/uploads/ava2.jpg",
                    celebrity_name="Benjamin Carroll",
                    celebrity_type="Actor",
                ),
                Celebrity(
                    anchor_url="#",
                    img_width=70,
                    img_height=70,
                    celebrity_url="images/uploads/ava3.jpg",
                    celebrity_name="Beverly Griffin",
                    celebrity_type="Actor",
                ),
                Celebrity(
                    anchor_url="#",
                    img_width=70,
                    img_height=70,
                    celebrity_url="images/uploads/ava4.jpg",
                    celebrity_name="Justin Weaver",
                    celebrity_type="Actor",
                ),
            ]
        )

    if not Trailer.objects.exists():
        Trailer.objects.bulk_create(
            [
                Trailer(trailer_url="https://www.youtube.com/embed/1Q8fG0TtVAY"),
                Trailer(trailer_url="https://www.youtube.com/embed/wVDtmouV9kM"),
                Trailer(trailer_url="https://www.youtube.com/embed/6ZfuNTqbHE8"),
                Trailer(trailer_url="https://www.youtube.com/embed/X4W2M-B73Vw"),
                Trailer(trailer_url="https://www.youtube.com/embed/eOrNdBpGMv8"),
                Trailer(trailer_url="https://www.youtube.com/embed/uisBaTkQAEs"),
            ]
        )

    if not TrailerItem.objects.exists():
        TrailerItem.objects.bulk_create(
            [
                TrailerItem(
                    img_src="images/uploads/trailer7.jpg",
                    img_alt="Wonder Woman",
                    img_width=100,
                    img_height=56,
                    description="Wonder Woman",
                    duration="2:30",
                ),
                TrailerItem(
                    img_src="images/uploads/trailer2.jpg",
                    img_alt="Oblivion",
                    img_width=100,
                    img_height=56,
                    description="Oblivion: Official Teaser Trailer",
                    duration="2:37",
                ),
                TrailerItem(
                    img_src="images/uploads/trailer6.jpg",
                    img_alt="Skull Island",
                    img_width=100,
                    img_height=56,
                    description="Exclusive Interview: Skull Island",
                    duration="2:44",
                ),
                TrailerItem(
                    img_src="images/uploads/trailer3.png",
                    img_alt="Logan",
                    img_width=100,
                    img_height=56,
                    description="Logan: Director James Mangold Interview",
                    duration="2:43",
                ),
                TrailerItem(
                    img_src="images/uploads/trailer4.png",
                    img_alt="Beauty and the Beast",
                    img_width=100,
                    img_height=56,
                    description="Beauty and the Beast: Official Teaser Trailer 2",
                    duration="2:32",
                ),
                TrailerItem(
                    img_src="images/uploads/trailer5.jpg",
                    img_alt="Fast & Furious 8",
                    img_width=100,
                    img_height=56,
                    description="Fast & Furious 8",
                    duration="3:11",
                ),
            ]
        )

    if not News.objects.exists():
        News.objects.bulk_create(
            [
                News(
                    section="featured",
                    img_src="images/uploads/blog-it1.jpg",
                    img_alt="featured news",
                    img_width=170,
                    img_height=250,
                    title="Brie Larson to play first female white house candidate Victoria Woodull in Amazon film",
                    content="Exclusive: Amazon Studios has acquired Victoria Woodhull, with Oscar winning Room star Brie Larson poised to produce and play the first female candidate for the presidency of the United States.",
                    time="13 hours ago",
                ),
                News(
                    section="left",
                    img_src="images/uploads/bloglist-it1.jpg",
                    img_alt="left news 1",
                    img_width=170,
                    img_height=250,
                    title="Michael Shannon Frontrunner to play Cable in Deadpool 2",
                    content="Industry reports indicate Michael Shannon has emerged as a lead candidate for Cable in Deadpool 2.",
                    time="13 hours ago",
                ),
                News(
                    section="left",
                    img_src="images/uploads/bloglist-it2.jpg",
                    img_alt="left news 2",
                    img_width=170,
                    img_height=250,
                    title="French horror Raw inspires theaters to hand out barf bags",
                    content="A Los Angeles theater chain offered barf bags to viewers during screenings of the film Raw.",
                    time="13 hours ago",
                ),
                News(
                    section="right",
                    img_src="images/uploads/bloglist-it3.jpg",
                    img_alt="right news 1",
                    img_width=170,
                    img_height=250,
                    title="Laura Dern in talks to join Justin Kelly biopic JT Leroy",
                    content="Laura Dern is in talks to join the cast of Justin Kelly's biopic JT Leroy.",
                    time="13 hours ago",
                ),
                News(
                    section="right",
                    img_src="images/uploads/bloglist-it4.jpg",
                    img_alt="right news 2",
                    img_width=170,
                    img_height=250,
                    title="China punishes more than 300 cinemas for box office cheating",
                    content="Authorities in China sanctioned more than 300 theaters after discovering manipulated box office totals.",
                    time="13 hours ago",
                ),
            ]
        )

    if not Tweet.objects.exists():
        Tweet.objects.bulk_create(
            [
                Tweet(
                    content="Just watched Interstellar again and I am still blown away by the visuals and emotion. #MovieNight #SciFi"
                ),
                Tweet(content="Wonder Woman trailer on repeat today. Who else is hyped?"),
            ]
        )


def remove_seed_data(apps, schema_editor):
    models_to_clear = [
        "Slider",
        "Advertisement",
        "SocialLink",
        "Trailer",
        "TrailerItem",
        "Celebrity",
        "News",
        "Tweet",
        "MovieTheater",
        "MovieTV",
    ]
    for model_name in models_to_clear:
        model = apps.get_model("app", model_name)
        model.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_seed_data),
    ]
