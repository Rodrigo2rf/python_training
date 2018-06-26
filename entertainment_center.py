#! /usr/bin/env python

import fresh_tomatoes
import media

alien = media.Movie('Alien','About the history','http://cdn1-www.comingsoon.net/assets/uploads/2017/05/Art-of-Alien-Covenant-e1495562562857.jpg','http://www.youtube.com/watch?v=LjLamj-b0I8')

movies = [alien]
fresh_tomatoes.open_movies_page(movies)
