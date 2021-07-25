import numpy as np
from manim import *
R = 8.314

class Main(ThreeDScene):
    def construct(self):
        # def get_p(t, v):
        #     return (R*t)/v
        # def get_v(t, p):
        #     return (R*t)/p
        # def get_t(p, v):
        #     return (p*v)/R
        # # p = z
        # # v = y
        # # t = x
        # def surface(x, y, z):
        #     p = get_p(x, y)
        #     v = get_v(x, z)
        #     t = get_t(z, y)
        #     return np.array([x, y, z], )

        threed = ParametricSurface(
            lambda u,v : np.array([
                v - 1,
                u - 1,
                u / v  # linearly prop to y axis, inversely prop to x axis
            ]),
            u_min=1, u_max=5, v_min=1, v_max=5
        ).rotate(90*DEGREES).scale(0.5)
        axis_config = {
            "x_range": (0, 5),
            "y_range": (0, 5),
            "z_range": (0, 5),
        }


        axis = ThreeDAxes(**axis_config).scale(0.5)
        axis.x_axis.set_color(RED)
        axis.y_axis.set_color(GREEN)
        axis.z_axis.set_color(BLUE)



        self.set_camera_orientation(
            phi=60*DEGREES,
            theta=30*DEGREES,
        )

        axis.center()
        self.add(axis, threed)

        # self.begin_ambient_camera_rotation()
        # self.wait(3)

        



        
        # self.begin_ambient_camera_rotation(rate=0.9)
        
        # self.wait(2)

# class Graph(Scene):
#     def construct(self):
#         axis = Axes(x_range=[-10, 10], y_range=[0, 1])

#         curve = axis.get_graph(
#             lambda x: 1 / (1 + e**(-1*x)), x_range=[-10, 10]
#         )
#         self.add(axis, curve)

