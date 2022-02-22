from manim import *

class poten(Scene):

    def construct(self):
        
        txt = Tex('How can i find half of $2^{10729027}$?')
        pot = MathTex('2^{10729027}').to_edge(LEFT*11)
        metade = MathTex('\\frac{x}{2}').to_edge(RIGHT*11)
        half = MathTex('\\frac{2^{10729027}}{2}')
        propriedade = MathTex('\\frac{a^{x}}{a^{y}} = a^{x-y}')
        text = Tex('Quotient of like bases')

        self.play(
            Create(
                txt
                 )
        )
        self.play(
            txt.animate.shift(UP*7),
            run_time = 6
        )
        
        self.play(
            Create(pot),
            Create(metade)
        )

        self.play(
            pot.animate.shift(LEFT * 5 + UP * 3),
            metade.animate.shift(RIGHT * 5 + UP * 3),
            run_time=3
        )
        self.play(
            # pot.animate.shift(RIGHT * 5 + DOWN * 3),
            pot.animate.set_opacity(0),
            Transform(pot,half),
            metade.animate.shift(LEFT*5 + DOWN*3),
            Transform(metade,half), 
            run_time=3
        )
        self.play(
          Unwrite(VGroup(pot, half, metade))
        )
        

        self.play(
            Create(text)
        )
        self.play(
            text.animate.shift(UP*1)    
        )

        propriedade.set_color_by_tex("a", RED)
        self.play(
            Create(propriedade)
        )