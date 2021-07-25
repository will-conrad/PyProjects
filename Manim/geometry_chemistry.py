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
        self.add(grid)
        wordproblem = Tex(
            "10.0 grams",
            " of ",
            "baking soda",
            " are mixed with an excess of ",
            "vinegar",
            " in a ",
            "2 liter",
            " bottle which is immediately sealed.  The reaction takes place at ",
            "20ºC",
            ".  Assuming the baking soda reacts completely, ",
            "what pressure will the CO$_{2}$ product be after the reaction?"
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

        # self.play(Write(wordproblem), run_time=5)
        # self.wait(1)
        # self.play(wordproblem.animate.shift(UP * 2.25))
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
        t = wordproblem[8].copy()
        l = wordproblem[6].copy()
        grams = Tex("10.0 g", " NaHCO$_3$").move_to([-1.7, 3, 0]).set_color(BLUE)
        temp = Tex("20 C").move_to([1.2, 3, 0])
        liters = Tex("2 L").move_to([2.9, 3, 0])
        self.play(
            FadeOut(wordproblem),
            sep.animate.shift(UP * 1.6),
            sep.animate.become(Line([-4, 2.6, 0], [4, 2.6, 0])),
            chemical_equation.animate.shift(DOWN * 3.5),
            Transform(g1, grams[0]),
            Transform(g2, grams[1]),
            Transform(l, liters),
            Transform(t, temp),
            # Transform(k, kpa),

        )
        grams.become(Tex("10.0 g NaHCO$_3$").move_to(grams))
        self.add(grams, temp, liters)
        self.remove(g1, g2, l, t)

        self.wait()

        to_mols = MathTex(r"\text{10.0 g NaHCO$_3$}",
                          r"\left(\frac{\text{1 mol NaHCO$_3$}}{\text{84.01 g NaHCO$_3$}}\right)",
                          " = ",
                          r"\text{0.119 mol NaHCO$_3$}")

        self.play(
            sep.animate.become(Line([-3.75, 2.6, 0], [3.75, 2.6, 0])),
            grams.animate.move_to(to_mols[0]),
            temp.animate.move_to([-2.8, 3, 0]),
            liters.animate.move_to([2.45, 3, 0]),
        )
        self.add(to_mols[0])
        self.remove(grams)
        self.wait(0.4)
        self.play(
            Write(to_mols[1])
        )
        self.wait(0.5)
        self.play(  # ==
            Write(to_mols[2]),
            Write(to_mols[3])
        )

        self.wait(1)
        to_co2 = MathTex(r"\text{0.119 mol NaHCO$_3$}",
                         r"\left(\frac{\text{1 mol CO$_2$}}{\text{1 mol NaHCO$_3$}}\right)",
                         " = ",
                         r"\text{0.119 mol CO$_2$}"
                         )
        mols = to_mols[3].copy()
        self.add(mols)
        self.remove(to_mols[3])

        self.play(
            FadeOut(to_mols[0:3]),
            mols.animate.move_to(to_co2[0])
        )
        self.add(to_co2[0])
        self.remove(mols)
        self.wait(0.1)
        self.play(
            Write(to_co2[1])
        )
        self.wait(0.1)
        self.play(
            Write(to_co2[2:4])
        )
        self.wait(1)

<<<<<<< HEAD:Manim/scene2.py
        mols = to_co2[3].copy()
        self.add(mols)
        self.remove(to_co2[3])
        self.play(
            sep.animate.become(Line([-5, 2.6, 0], [5, 2.6, 0])),
            mols.animate.move_to([-3.7, 3, 0]),
=======
        self.play(      N  )),
            to_mols[3].animate.move_to([-3.7, 3, 0]),
>>>>>>> origin/main:Manim/geometry_chemistry.py
            temp.animate.move_to([-1.4, 3, 0]),
            liters.animate.move_to([3.8, 3, 0]),
            FadeOut(to_co2[0:3]),
            chemical_equation.animate.shift(DOWN).set_opacity(0)
        )

        self.wait()
        #====================================================
        to_kelvin = Tex("20 C",
                        " $+$ ",
                        "273.2",
                        " = ",
                        "293.2 K"
                        )
        # in_cel = to_kelvin[0].copy()

        self.play(
            sep.animate.become(Line([-3.75, 2.6, 0], [3.75, 2.6, 0])),
            temp.animate.move_to(to_kelvin[0]),
            mols.animate.move_to([-2.4, 3, 0]),
            liters.animate.move_to([2.6, 3, 0]),
        )
        self.add(to_kelvin[0])
        self.remove(temp)
        self.wait(0.3)
        self.play(
            Write(to_kelvin[1]),
            Write(to_kelvin[2])
        )
        self.wait(0.3)
        self.play(
            Write(to_kelvin[3]),
            Write(to_kelvin[4])
        )

        self.wait(1)

        kelvin = to_kelvin[4].copy()
        self.add(kelvin)
        self.remove(to_kelvin[4])
        self.play(
            sep.animate.become(Line([-5, 2.6, 0], [5, 2.6, 0])),
            kelvin.animate.move_to([-3.8, 3, 0]),
            mols.animate.move_to([0, 3, 0]),
            liters.animate.move_to([3.8, 3, 0]),
            FadeOut(to_kelvin[0:4])
        )
        self.wait(1)
        # ===============================================
        gas_law = MathTex("P", "V", "=", "n", "R", "T").scale(2)
        # PV=nRT
        # 012345
        solve_for_pressure = MathTex("P", "=", "{", "n", "R", "T\over", "V}").scale(2)
        self.play(
            Write(gas_law)
        )
        self.wait()
        self.play(
            Transform(gas_law[0], solve_for_pressure[0], replace_mobject_with_target_in_scene=True),
            Transform(gas_law[1], solve_for_pressure[6], replace_mobject_with_target_in_scene=True),
            Transform(gas_law[2], solve_for_pressure[1], replace_mobject_with_target_in_scene=True),
            Transform(gas_law[3], solve_for_pressure[3], replace_mobject_with_target_in_scene=True),
            Transform(gas_law[4], solve_for_pressure[4], replace_mobject_with_target_in_scene=True),
            Transform(gas_law[5], solve_for_pressure[5], replace_mobject_with_target_in_scene=True),
        )
        # self.play(
        #     Transform(gas_law[0], solve_for_pressure[0]),
        #     Transform(gas_law[1], solve_for_pressure[5]),
        #     Transform(gas_law[2], solve_for_pressure[1]),
        #     Transform(gas_law[3], solve_for_pressure[2]),
        #     Transform(gas_law[4], solve_for_pressure[3]),
        #     Transform(gas_law[5], solve_for_pressure[4]),
        # )

        # self.remove(solve_for_pressure[0],
        #             solve_for_pressure[1],
        #             solve_for_pressure[2],
        #             solve_for_pressure[3],
        #             solve_for_pressure[4],
        #             solve_for_pressure[5])
        # self.remove(gas_law[0],
        #             gas_law[1],
        #             gas_law[2],
        #             gas_law[3],
        #             gas_law[4],
        #             gas_law[5])
        # self.remove(
        #     solve_for_pressure[1]
        # )
        self.wait()
        final = MathTex("P",
                        "=",
                        r"{",
                        r"0.119 \text{ mol}",
                        r"\cdot",
                        r"8.315\left(\frac{L\cdot kPa}{K\cdot mol}\right)",
                        r"\cdot",
                        r"293.2\text{ K}\over",
                        r"2\text{ L}}").scale(1.5).shift(UP* 0.1)

        self.play(
            # P to P
            Transform(solve_for_pressure[0], final[0]),

            # = to =
            Transform(solve_for_pressure[1], final[1]),
            Transform(solve_for_pressure[3], final[3]),
            # R to R
            Transform(solve_for_pressure[4], final[5]),
            solve_for_pressure[3].animate.set_opacity(0).scale(0.5),
            solve_for_pressure[5].animate.set_opacity(0).scale(0.5),
            solve_for_pressure[6].animate.set_opacity(0).scale(0.5),
            Transform(mols, final[3]),
            Transform(liters, final[8]),
            Transform(kelvin, final[7])

        )


            # Transform(mols, final[2]),
            # FadeIn(final[3]),
            # Write(final[4]),
            # FadeIn(final[5]),
            # Transform(kelvin, final[6]),
            # Transform(liters, final[7]),

        # )

