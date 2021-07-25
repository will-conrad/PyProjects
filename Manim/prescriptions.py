from manim import *

class Main(Scene):

    def construct(self):
        x = [
            "1/17/2018",
            "1/28/2019",
            "3/29/2021",
            "6/29/2021"
        ]
        data = [
            ["a", "b", "c"],
            ["x", "y", "z"]
        ]
        axes = Axes(
            y_range=[-3, 3],
            x_range=[0, 5],
            y_axis_config={"label_direction": LEFT},
            x_axis_config={"label_direction": DOWN}
        )
        labels = axes.get_axis_labels(
            y_label=Tex("Diopters"),
            x_label=Tex("Date")
        )
        self.add(axes, labels)
        # values_x = [
        #     (3.5, "3.5"),  # (position 3.5, label "3.5")
        #     (4.5, "\\frac{9}{2}")  # (position 4.5, label "9/2")
        # ]
