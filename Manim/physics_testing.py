from manim import *
from manim_physics import *
#config.pixel_width = 1000
#config.pixel_height = 1000
class Filling(SpaceScene):
	def construct(self):
		# config.frame_width =
		# config.frame_height = 9

		grid = NumberPlane(x_range=[-7, 7], y_range=[-7, 7])
		self.add(grid)


		shade1 = Rectangle(height = 2, width = 10).shift(UP * 6).set_fill(BLACK, 1).set_stroke(color=BLACK)
		ground = Line([-5, -5, 0], [5, -5, 0])
		top = Line([-5, 5, 0], [5, 5, 0])
		wall1 = Line([-5, -5, 0], [-5, 5, 0])
		wall2 = Line([5, -5, 0], [5, 5, 0])
		walls = VGroup(shade1, ground, top, wall1, wall2)
		self.add(walls)

		circle1 = Circle(radius=0.5)
		circle2 = Circle(radius=0.75).shift(UR * 4)
		circle3 = Circle(radius=0.5).shift(RIGHT * 3)
		circle4 = Circle(radius=0.3).shift(UP * 4)
		circle5 = Circle(radius=0.8).shift(RIGHT * 1.5)
		balls = VGroup(circle1, circle3, circle4, circle5)
		self.add(balls)


		self.make_rigid_body(circle1, circle3, circle4, circle5)
		self.make_static_body(walls)
		self.wait(5)