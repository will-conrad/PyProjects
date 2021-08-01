from manim import *

class Main(Scene):
	def construct(self):
		def get_steps(width, height, steps):
			# Adds left L shape of steps
			points = [
				[width,0,0],
				[0,0,0],
				[0,height,0]
			]
			# Keep track of x and y of points
			x = 0
			y = height
			for n in range(steps):
				# move over right
				x += width/steps
				# Add point
				points.append([x, y, 0])

				# Move down
				y -= height/steps
				# Add point
				points.append([x, y, 0])
			
			# Create shape from points
			shape = Polygon(*points).move_to(ORIGIN)
			# return steps and numbers
			return VGroup(shape,
			              Tex(width).next_to(shape, DOWN),
			              Tex(height).next_to(shape, LEFT))
			
		
		# Add steps object
		self.add(get_steps(width=5, height=5, steps=3))

