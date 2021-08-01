from manim import *
RAD = PI / 180

class CircleTriangle(Scene):
    def construct(self):
        r = 3.5
        buffer = 1 + MED_SMALL_BUFF
        angle_track = ValueTracker(0)

        circle = Circle(radius=r)
        center, top = Dot(circle.get_center()), Dot([0, r, 0])
        circum = Dot([r, 0, 0])
        radius1 = Line(circle.get_center(), [0, r, 0]).set_stroke(width=5, color=GREEN)
        radius2 = Line(circle.get_center(), [r, 0, 0]).set_stroke(width=5, color=BLUE)
        hyp = Line(top, circum).set_stroke(width=5, color=YELLOW)
        moving = VGroup(radius2, circum)
        moving_ref = moving.copy()

        moving.rotate(
            angle_track.get_value() * RAD, about_point=ORIGIN
        )
        angle = Angle(radius1, radius2, radius=0.75, other_angle=True).set_stroke(width=5)
        tex = MathTex(r"\theta").move_to(
            Angle(
                radius1, radius2, radius=buffer, other_angle=True
            ).point_from_proportion(0.5)
        )

        angle.add_updater(
            lambda x: x.become(Angle(radius1, radius2, radius=0.75, other_angle=True).set_stroke(width=5))
        )
        hyp.add_updater(
            lambda x: x.become(Line(top.get_center(), circum.get_center()).set_stroke(width=5, color=YELLOW))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    radius1, radius2, radius=buffer, other_angle=True
                ).point_from_proportion(0.5)
            )
        )
        moving.add_updater(
            lambda x: x.become(moving_ref).rotate(
                angle_track.get_value() * RAD, about_point=ORIGIN
            )
        )

        self.add(circle, angle, radius1, hyp, moving, top, center, tex)
        self.play(
            Rotating(moving, about_point=ORIGIN, radians=PI * -2, rate_func=smooth)

        )
