from manim import *
from manimlib import *
from random import *

class Main(Scene):
  def construct(self):
    r = 3
    c = Circle(r).set_color(WHITE)
    self.add(c)
    dot = Dot().shift(RIGHT * (random() * (r - 1) + 0.5)).rotate(random() * 360 * DEGREES, about_point=c.get_center())
    # dot.move_to([2, 0, 0])
    
    lines = VGroup(
      *[
        Line(start=dot.get_center(), end=c.point_at_angle(5 * i * DEGREES)).set_stroke(width=1)for i in range(72)
      ]
    )
    bgLines = lines.copy()
    for i in bgLines:
      i.set_stroke(opacity=0.3)
    
    self.add(bgLines, lines)
    self.wait()
    self.play(
      LaggedStart(*[i.animate.rotate(90 * DEGREES)for i in lines], lag_ratio=0.15),
      run_time=6
    )
    
