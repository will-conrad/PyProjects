from manim import *

class sequence(Scene):
	def construct(self):

		for n in range(1,10):
			mgon = RegularPolygon(n)
			ngon = RegularPolygon(n+1)
			self.add(mgon)

			self.play(
				mgon.rotate(-PI / n),
				Transform(mgon, ngon, replace_mobject_with_target_in_scene=True)
			)
			self.remove(ngon)





		# dot1 = Dot(ORIGIN).scale(1.5)
		# dot2 = Dot(ORIGIN).scale(1.5).set_color(BLUE)
		# dot3 = Dot([-1.155, -1, 0]).scale(1.5).set_color(RED )
		# line = Line(UP, DOWN).set_stroke(width=4).set_opacity(0)
		#
		# triangle1 = Polygon([0, 1, 0],[0, 1, 0],[0, -1, 0]).set_color(WHITE).set_opacity(0)
		# triangle2 = Polygon([-1.155, -1, 0], [0, 1, 0], [1.155, -1, 0]).set_color(WHITE)
		#
		# self.add(triangle1, line, dot2, dot1)
		#
		# self.play(ApplyMethod(dot1.set_color, RED, run_time=0.5))
		# line.set_opacity(100)
		# self.play(
		# 	GrowFromCenter(line),
		# 	ApplyMethod(dot1.shift, UP),
		# 	ApplyMethod(dot2.shift, DOWN)
		# )
		# self.remove(line)
		# self.add(triangle1)
		#
		# self.play(
		# 	Transform(dot1, dot3),
		# 	Transform(triangle1, triangle2),
		# 	ApplyMethod(dot2.shift, RIGHT * 1.155)
		# )

