from manim import *

class Main(Scene):
    def construct(self):
        ball = VGroup(Circle(1), Dot().shift(UP))
        ground = Line([-7, -1, 0], [7, -1, 0])
        self.add(ball, ground)
        self.play(
            ball.animate.shift(RIGHT*(2 * PI)),
            ball.animate.rotate(angle = (2 * PI), about_point=ORIGIN)
        )