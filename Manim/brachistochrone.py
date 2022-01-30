from manim import *

config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1280
config.pixel_height = 720

width = config.frame_width

class Main(Scene):
  def construct(self):
    floor = Line([width / -2, 0, 0], [width / 2, 0, 0])
    floor.shift(DOWN*2)
    floor.set_stroke(width=5)
    p = ValueTracker(0)
    self.add(floor)

    roller = Circle(1.5).shift(DOWN*0.5 + LEFT * 6).set
    self.add(roller)
    

    self.wait()