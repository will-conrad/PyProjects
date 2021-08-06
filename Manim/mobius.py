from manim import *
from numpy import sin, cos
class Main(ThreeDScene):
    def construct(self):
        axis = Axes()

        self.set_camera_orientation(
            phi=0 * DEGREES,
            theta=0 * DEGREES,
        )

        axis.center()
        mobius_strip = ParametricSurface(
            lambda u, v: np.array([
                (1 + v * cos(u / 2)) * cos(u),
                (1 + v * cos(u / 2)) * sin(u),
                v * sin(u / 2)
                # ((1 + v / 2) * (np.cos(u / 2))) * np.cos(u),
                # ((1 + v / 2) * (np.cos(u / 2))) * np.sin(u),
                # (v / 2) * np.sin(u / 2)
            ]), v_min=-1, v_max=1, u_min=0, u_max=PI * 2
        )
        self.add(mobius_strip)

        self.begin_ambient_camera_rotation()
        self.move_camera(
            phi=60 * DEGREES
        )

        self.wait(10)