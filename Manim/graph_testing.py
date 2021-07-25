from manim import *

class Plot5(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):



        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        values_x = [
            (3.5, "3.5"),  # (position 3.5, label "3.5")
            (4.5, r"\frac{9}{2}")  # (position 4.5, label "9/2")
        ]
        self.x_axis_labels = VGroup()  # Create a group named x_axis_labels
        #   pos.   tex.
        for x_val, x_tex in values_x:
            tex = MathTex(x_tex)  # Convert string to tex
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)  # Put tex on the position
            self.x_axis_labels.add(tex)  # Add tex in graph
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )




        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            Create(graph),
            run_time = 2
        )
        self.wait()

