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
                                            tolerance=0.1,
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
        # o = Circle(3)
        # op = Dot().move_to(o.get_center())
        # o1 = Circle(0.8)
        # a = Dot()
        # ang = 110 * DEGREES
        # o1.circle_to_inside_circumfrence(o, ang)
        # a.to_point_along_circle(o, ang)
        # o1p = Dot().move_to(o1.get_center())
        # o1pl = Line(o1.get_center(), o1p.get_center())
        # p = Dot()
        # p.to_point_along_circle(o1, 220 * DEGREES)
        # pl = o1pl.copy().rotate(90 * DEGREES).move_to(o1p)
        # oa = Line(o.get_center(), a.get_center())
        # oap = oa.copy().rotate(90 * DEGREES).move_to(a)

        # self.add(o, a, op, o1, o1p, p, oa, oap, o1pl, pl)
        # self.bring_to_front(a)
        def line_tan_to_point(circle, point):
            return Line(circle.get_center(), point.get_center()).set_length(20).rotate(90*DEGREES).move_to(point)

        O = Circle(3)
        pO = Dot().move_to(O)

        O1 = Circle(0.8)
        O1.circle_to_inside_circumfrence(O, 110 * DEGREES)
        pO1 = Dot().move_to(O1)

        P = Dot()
        P.to_point_along_circle(O1, 230 * DEGREES)

        self.add(O, pO, O1, pO1, P)

        A = Dot()
        A.to_point_along_circle(O1, 110 * DEGREES)
        tanLineP = line_tan_to_point(O1, A)
        tanLineA = line_tan_to_point(O1, P)
        lOA = Line(pO.get_center(), A.get_center()).set_length(20)
        lAP = Line(A.get_center(), P.get_center()).move_to(self.get_intersections(tanLineA, tanLineP)).set_length(20)



        self.add(A, lOA, tanLineP,tanLineA, lAP)




