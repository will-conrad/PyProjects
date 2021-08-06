from manim import *
import numpy as np
class ThreeDLightSourcePosition(ThreeDScene):
    def construct(self):
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u),
                1.5 * np.cos(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)
        )
        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(sphere)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(4)