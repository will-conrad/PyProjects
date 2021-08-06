from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Tex("Hello world!")
        self.play(
            Write(text)
        )
        self.wait()