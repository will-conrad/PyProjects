from manim import *
from math import e
from numpy import linspace
p = 10**-5

class Main(Scene):
    def construct(self):
        # text1 = Tex("Sigmoid Curve").scale(1.6).align_on_border(UL, buff=1)
        t = ValueTracker(-8)
        grid = NumberPlane(x_range=[-8-p, 8+p, 0.5], y_range=[0, 1+p, 2], y_length=6.5, x_length=12.5).shift(UP*0.2)
        ax = Axes(x_range=[-8, 8, 0.5], y_range=[0, 1, 2], y_length=6.5, x_length=12.5, tips=False).shift(UP*0.2).set_opacity(0)
        labels = VGroup(*[Tex(str(x)).move_to(ax.coords_to_point(x, 0)).shift(DOWN*0.35) for x in range(-8, 9, 2)],
                        *[Tex(str(y)).move_to(ax.coords_to_point(0, y)).shift(DR*0.4) for y in linspace(0.5, 1, 2)])
        sigmoid_graph = ax.get_graph(lambda x: 1/(1+(e**-x)), x_range=[-8, 8])

        self.play(
            LaggedStart(
                Create(grid),
                Create(labels),
                lag_ratio=0.2,
                run_time=2
            ),
        )
        self.play(
            Create(sigmoid_graph)
        )
        initial_point = [ax.coords_to_point(t.get_value(), sigmoid(t.get_value()))]
        dot = Dot(point=initial_point, radius=0.125)

        dot.add_updater(lambda x: x.move_to(ax.coords_to_point(t.get_value(), sigmoid(t.get_value()))))
        self.play(
            DrawBorderThenFill(dot)
        )
        self.wait(0.5)

        self.play(
            t.animate.set_value(8),
            run_time=5
        )