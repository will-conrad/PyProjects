from manim import *
import numpy as np
import math

class MoveBracesCopy(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff = SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff = SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
        	ReplacementTransform(brace1.copy(),brace2),
        	ReplacementTransform(t1.copy(),t2)
        	)
        self.wait()


class AnimatingMethods(Scene):
    def construct(self):

        grid = MathTex("\\pi").get_grid(10, 10, height=4)
        self.add(grid)

        # You can animate the application of mobject methods with the
        # ".animate" syntax:
        self.play(grid.animate.shift(LEFT))

        # Alternatively, you can use the older syntax by passing the
        # method and then the arguments to the scene's "play" function:


        # Both of those will interpolate between the mobject's initial
        # state and whatever happens when you apply that method.
        # For this example, calling grid.shift(LEFT) would shift the
        # grid one unit to the left, but both of the previous calls to
        # "self.play" animate that motion.

        # The same applies for any method, including those setting colors.
        self.play(grid.animate.set_color(YELLOW))
        self.wait()
        self.play(grid.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
        self.wait()
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()
        #
        # # The method Mobject.apply_complex_function lets you apply arbitrary
        # # complex functions, treating the points defining the mobject as
        # # complex numbers.
        plane = NumberPlane()
        self.add(plane)
        self.play(
            grid.animate.apply_complex_function(np.exp),
            plane.animate.apply_complex_function(np.exp),
            run_time=5)
        self.wait()
        #
        # # Even more generally, you could apply Mobject.apply_function,
        # # which takes in functions form R^3 to R^3
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 1 * math.sin(p[1]),
                    p[1] + 1 * math.sin(p[0]),
                    p[2]
                ]
             ),
            plane.animate.apply_function(
                lambda p: [
                    p[0] + 1 * math.sin(p[1]),
                    p[1] + 1 * math.sin(p[0]),
                    p[2]
                ]
            ),
            run_time=5,
        )
        self.wait()

class Testing(Scene):
    def construct(self):
        code = Code("/Users/willconrad/PyProjects/Manim/HelloWorld.py", language="py")
        self.play(Create(code))
        self.wait()



