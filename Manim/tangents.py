from manim import *
import numpy as np

class GetIntersections:
    def get_coord_from_proportion(self,vmob,proportion):
        return vmob.point_from_proportion(proportion)

    def get_points_from_curve(self, vmob, dx=0.005):
        coords = []
        for point in np.arange(0, 1 + dx, dx):
            dot = Dot(self.get_coord_from_proportion(vmob,point))
            coords.append(dot.get_center())
        return coords

    def get_intersections(self, vmob1, vmob2,
                                            tolerance=0.01,
                                            radius_error=0.2,
                                            use_average=True,
                                            use_first_vmob_reference=False):
        coords_1 = self.get_points_from_curve(vmob1)
        coords_2 = self.get_points_from_curve(vmob2)
        intersections = []
        for coord_1 in coords_1:
            for coord_2 in coords_2:
                distance_between_points = np.linalg.norm(coord_1 - coord_2)
                if use_average:
                    coord_3 = (coord_2 - coord_1) / 2
                    average_point = coord_1 + coord_3
                else:
                    if use_first_vmob_reference:
                        average_point = coord_1
                    else:
                        average_point = coord_2
                if len(intersections) > 0 and distance_between_points < tolerance:
                    last_intersection=intersections[-1]
                    distance_between_previus_point = np.linalg.norm(average_point - last_intersection)
                    if distance_between_previus_point > radius_error:
                        intersections.append(average_point)
                if len(intersections) == 0 and distance_between_points < tolerance:
                    intersections.append(average_point)
        return intersections

class Main(Scene, GetIntersections):
    def construct(self):
        circle = Circle(radius=1).set_color(GREEN)
        circle2 = Circle(radius=0.5).set_color(RED).next_to(circle, buff=0)
        circle3 = Circle(radius=0.25).set_color(BLUE).next_to(circle2, buff=0.035)
        circle3.rotate(0 * DEGREES, about_point=circle2.get_center())
        # line_1 = TangentLine(circle, alpha=0.0, length=4, color=BLUE_D)  # right
        # line_2 = TangentLine(circle, alpha=0.5, length=5, color=GREEN)  # left
        # line_3 = TangentLine(circle, alpha=0.75, length=5, color=YELLOW)  # bottom
        # dot = Dot(1).move_to(self.get_intersections(line_2, line_3))

        # self.bring_to_back(dot)

        self.add(circle, circle2, circle3)
        circle2.add_updater(lambda c: c.next_to(circle, buff=0))
        circle3.add_updater(lambda c: c.next_to(circle2, buff=0))

        self.play(
            Rotating(circle2, about_point=circle.get_center(), run_time=2),
            Rotating(circle3, about_point=circle.get_center(), run_time=2)
        )


