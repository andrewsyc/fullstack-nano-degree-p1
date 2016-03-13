__author__ = 'andrewsyc'
import webbrowser


class Movie():
    """
    Creates an individual movie listing for each instance, takes arguments of the Movie Title,
    Storyline, Theatrical Poster, and Youtube Trailer link for the pop up.
    """
    VALID_RATINGS = ["G","PG","PG-13","R"]

    #Takes in 4 arguments needed for movie listing, movie title, storyline, theatrical image, youtube link.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #If called this automatically opens a default web browser to the url argument.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)