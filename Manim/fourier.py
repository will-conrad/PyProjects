from manim import *
from numpy import linspace


class Fourier(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 2],
                  y_range=[-1.25, 1.25],
                  y_axis_config={"numbers_with_elongated_ticks": range(-1, 2)},
                  tips=False)
        labels = VGroup(*[Tex(str(x)).move_to(ax.coords_to_point(x, 0)).shift(DOWN*0.35) for x in [0.5, 1.5]],
                        *[Tex(str(y) if y % 1 != 0 else str(int(y))).move_to(ax.coords_to_point(0, y)).shift(LEFT*0.6) for y in linspace(-1, 1, 5)])
        self.add(ax, labels)


        # def fourier(x):
        #     a = ((4/PI)*(1/index)*np.sin(index*PI*x))
        #     a += total
        #     return a




        # self.play(
        #     LaggedStart(*[
        #         Create(ax.get_graph(lambda x: sum(((4/PI)*(1/n)*np.sin(n*PI*x)))))
        #         for n in range(1, 18, 2)],
        #         lag_ratio=0.5
        #     )
        # )

        # self.play(
        #     Create(ax.get_graph(lambda x: sum([
        #         (4 / PI) * (1 / n) * np.sin(n * PI * x) for n in range(1, 4)]
        #     )))
        #
        # )
        sum = 0
        for z in range(1, 10, 2):
            w = z + 2
            graph1 = ax.get_graph(lambda x: (4 / PI) * (1 / z) * np.sin(z * PI * x))
            graph2 = ax.get_graph(lambda x: ((4 / PI) * (1 / w) * np.sin(w * PI * x)) + graph1)

            self.play(
                ReplacementTransform(graph1, graph2)
            )