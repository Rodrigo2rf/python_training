#! /usr/bin/env python

import webbrowser

class Movie():

	# cria espaco em memoria para a instancia da clase
	def __init__(self, title, storyline, poster, trailer):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
