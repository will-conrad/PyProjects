from manim import *

class Main(Scene):
    def construct(self):
        square = Square(1)

        text = Tex("Y= ").shift(RIGHT*3)
        self.add(text)
        tracker = ValueTracker(0)
        square.add_updater(
        	lambda x: x.set_y(tracker.get_value())
        )
        label = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
                .set_value(tracker.get_value())
                .next_to(text, RIGHT, buff=0.1)
        )





        self.add(square, label)
        self.play(
        	tracker.animate.set_value(3)
        )
        self.wait()