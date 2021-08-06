from manim import *
from manim_physics import *

class BouncingBall(SpaceScene):
	def construct(self):
		boundary = Circle(radius=3.5).
		dot = Circle(radius=0.1)
		self.add(boundary, dot)
		self.make_static_body(boundary)
		self.make_rigid_body(dot)
		self.wait(3)