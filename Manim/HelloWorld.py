from manim import *

class HelloWorld(Scene):
    def construct(self):
        s = Square(3)
        self.add(s)
        self.wait()
        s.rotate(10*DEGREES)
        self.wait()
        s.rotate(10 * DEGREES)
        self.wait()