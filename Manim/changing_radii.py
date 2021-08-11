from manim import *

class Main(Scene):
    def construct(self):
        r1 = ValueTracker(2)
        r2 = ValueTracker(2)
        d1 = ValueTracker(4)
        d2 = ValueTracker(4)
        d1.add_updater(lambda g: g.set_value(r1.get_value() * 2))
        d2.add_updater(lambda h: h.set_value(r2.get_value() * 2))
        bound = Rectangle(height=max(d1.get_value(), d2.get_value()), width=d1.get_value() + d2.get_value())
        c1 = Circle(r1.get_value()).shift(LEFT * ((r1.get_value() + r2.get_value()) / 2))
        c2 = Circle(r2.get_value()).shift(RIGHT * ((r1.get_value() + r2.get_value()) / 2))
        c1.add_updater(lambda n : n.become(Circle(r1.get_value()).shift(LEFT * ((r1.get_value() + r2.get_value()) / 2))))
        c2.add_updater(lambda n: n.become(Circle(r2.get_value()).shift(RIGHT * ((r1.get_value() + r2.get_value()) / 2))))
        bound.add_updater(lambda l: l.become(Rectangle(height=max(d1.get_value(), d2.get_value()), width=d1.get_value() + d2.get_value())))
        self.add(c1, c2, bound)
        self.play(
            r1.animate.set_value(3),
            r2.animate.set_value(2)
        )