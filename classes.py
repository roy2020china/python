#
import webbrowser

class Movie():
	def __init__(self, title, storyline, trailerurl, movieurl):
		self.title = title
		self.storyline = storyline
		self.trailerurl = trailerurl
		self.movieurl = movieurl
	def openmovietrailer(self):
		webbrowser.open(self.trailerurl)
