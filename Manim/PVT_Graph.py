from manim import *

class main(ThreeDScene):
    def construct(self):
        axis = ThreeDAxes(x_range=[0, 10], y_range=[0, 10], z_range=[0, 10]).scale(0.5)
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)


        self.add(axis)
