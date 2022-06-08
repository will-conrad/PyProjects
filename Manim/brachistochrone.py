from cProfile import run
from cairo import Gradient
from manim import *

config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60

width = config.frame_width

class Main(Scene):
  def construct(self):
    floor = Line([width / -2, 0, 0], [width / 2, 0, 0])
    floor.shift(DOWN*2)
    floor.set_stroke(width=5)
    p = ValueTracker(0)
    self.add(floor)

    roller = Circle(1.5).shift(DOWN*0.5 + LEFT * 6).set_fill(color=color_gradient([RED, BLUE], length_of_output=100), opacity=1)
    roller.add_updater(
      lambda mob : mob.move_to(floor.point_from_proportion(p.get_value())).shift(UP * 1.5).rotate(-0.1)
      )
    
    self.add(roller)
    

    self.play(p.animate(rate_func=linear).set_value(1), run_time=3)
