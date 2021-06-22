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

class Chemistry(Scene):
    def construct(self):
        grid = NumberPlane().set_opacity(50)
        # self.add(grid)
        wordproblem = Tex(
            "10 grams",
            " of ",
            "baking soda",
            " are mixed with an excess of ",
            "vinegar",
            " in a ",
            "2 liter",
            " bottle which is immediately sealed.  The reaction starts at ",
            "101.3 kPa",
            " and takes place at ",
            "20ºC",
            ".  Assuming the baking soda reacts completely, ",
            "What pressure will the CO$_{2}$ product be after the reaction?"
        ).center().scale(0.8)


        chemical_equation = Tex(
            "NaHCO$_3$",
            " + ",
            "HC$_2$H$_3$O$_2$",
            " $\\rightarrow$ ",
            "NaC$_2$H$_3$O$_2$",
            " + ",
            "CO$_2$",
            " + ",
            "H$_2$O"
        ).move_to([0, 0.3, 0])
        sep = Line([-6.5, 1, 0], [6.5, 1, 0])

        self.wait(1.5)

        self.play(Write(wordproblem), run_time=5)
        self.wait(1)
        self.play(wordproblem.animate.shift(UP * 2.25))
        self.wait(0.1)

        self.play(Create(sep))
        bs = wordproblem[2].copy()
        v = wordproblem[4].copy()
        self.play(
            Transform(bs, chemical_equation[0]),
            Transform(v, chemical_equation[2])
        )
        self.play(
            Write(chemical_equation[1]),
            Write(chemical_equation[3:9])
        )
        self.add(chemical_equation)
        self.remove(bs, v)

        self.wait(2)
        g1 = wordproblem[0].copy()
        g2 = wordproblem[2].copy()
        t = wordproblem[10].copy()
        k = wordproblem[8].copy()
        l = wordproblem[6].copy()
        grams = Tex("10g", " NaHCO$_3$").move_to([-3.8, 3, 0])
        temp = Tex("20ºC").move_to([-0.9, 3, 0])
        kpa = Tex("101.3 kPa").move_to([1.6, 3, 0])
        liters = Tex("2 Liters").move_to([4.3, 3, 0])
        self.play(
            FadeOut(wordproblem),
            sep.animate.shift(UP * 1.6),
            sep.animate.become(Line([-5.5, 2.6, 0], [5.5, 2.6, 0])),
            chemical_equation.animate.shift(DOWN * 3.5),
            Transform(g1, grams[0]),
            Transform(g2, grams[1]),
            Transform(l, liters),
            Transform(t, temp),
            Transform(k, kpa),

        )
        grams.become(Tex("10g NaHCO$_3$").move_to([-3.8, 3, 0]))
        self.add(grams, temp, kpa, liters)
        self.remove(g1, g2, l, k, t)

        self.wait()

        to_mols = MathTex(r"\text{10g NaHCO$_3$}",
                          r"\left(\frac{\text{1 mol NaHCO$_3$}}{\text{84.01g NaHCO$_3$}}\right)",
                          " = ",
                          r"\text{0.119mol}",
                          r"\text{ NaHCO$_3$}")
        in_grams = to_mols[0].copy()
        self.play(
            sep.animate.become(Line([-3.75, 2.6, 0], [3.75, 2.6, 0])),
            grams.animate.move_to(in_grams),
            kpa.animate.move_to([-0.3, 3, 0]),
            temp.animate.move_to([-2.8, 3, 0]),
            liters.animate.move_to([2.45, 3, 0]),
        )
        self.wait(0.4)
        self.play(
            Write(to_mols[1])
        )
        self.wait(0.5)
        self.play(
            Write(to_mols[2]),
            Write(to_mols[3]),
            Write(to_mols[4])
        )
        self.wait(1)

        self.play(
            sep.animate.become(Line([-5, 2.6, 0], [5, 2.6, 0])),
            to_mols[3].animate.move_to([-3.7, 3, 0]),
            temp.animate.move_to([-1.4, 3, 0]),
            kpa.animate.move_to([1, 3, 0]),
            liters.animate.move_to([3.8, 3, 0]),
            FadeOut(grams),
            FadeOut(to_mols[1:3]),
            FadeOut(to_mols[4])
        )

        self.wait()