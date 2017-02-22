import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url
    def open_trailer(self):
        webbrowser.open(self.trailer_url)
