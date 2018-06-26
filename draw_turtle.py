#! /usr/bin/env python

import turtle

def draw_square():
	
	screen = turtle.Screen()
	# screen.setup(width=200, height=200, startx=0, starty=0)
	screen.title('My Screen')
	
	a = turtle.Turtle()
	a.pensize(1)
	a.speed(10)
	for y in range(90):
		for x in range(4):
			a.right(y * 5)
			a.forward(150)
			a.right(90 - (y * 5))

	screen.exitonclick()


draw_square()
