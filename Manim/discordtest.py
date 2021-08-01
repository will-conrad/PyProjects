from manim import *
import numpy as np


class Graph(Scene):
    def construct(self):
        axes = Axes(x_range=[-2,-5], y_range=[14,5])
        self.play(Write(axes, lag_ratio = 0.01,run_time = 1))


        ln_sin_graph = axes.get_graph(
            lambda x : np.log(x)*np.sin(x),
            color = BLUE,
        )

        ln_sin_label = axes.get_graph_label(ln_sin_graph,"\ln(x)sin(x)")

        self.play(
            Create(ln_sin_graph),run_time = 2
        )