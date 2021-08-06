from manim import *
# config.background_color = WHITE
from math import sqrt

from numpy import sin, cos

class Circles(Scene):
    def construct(self):
        def triangle_coords(x, y, t, l):
            R = l / sqrt(3)
            a = [R * cos(t), R * sin(t), 0]
            b = [R * cos(t + ((4 * PI) / 3)), R * sin(t + ((4 * PI) / 3)), 0]
            c = [R * cos(t + ((2 * PI) / 3)), R * sin(t + ((2 * PI) / 3)), 0]


            return [a, b, c]

        main = Circle(PI)
        triangle = Polygon(*triangle_coords(0, 0, 90 * DEGREES, PI))
        self.add(main, triangle)


