from manim import *
from math import sqrt

class Main(Scene):
	def construct(self):
		def inscribe(d, x):
			self.play(
				Create(Square(d)),
				run_time=0.2
			)
			self.play(
				Create(Circle(d/2)),
				run_time=0.2
			)
			
			d = (d/2) * sqrt(2)
			x += 1
			if x < 20:
				inscribe(d, x)
		inscribe(10, 1)
		
			
		