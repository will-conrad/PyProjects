from manim import *
 
class AnimatedBezier(Scene):
  def __init__(self, pts = [ORIGIN], colors=["#FFFFFF"]):
    self.pts = pts
    self.colors = colors
  def create_beziers(self):
    pts = np.array(self.pts)
    colors = self.colors
    t = ValueTracker(0)
    points = VGroup(*[Dot(i, radius=0.1).set_fill(color=config.background_color).set_stroke(colors[0], 3, 1)for i in pts]) 
    points[0].set_fill(colors[0])
    lines = VGroup(*[Line(pts[i], pts[i+1]).set_stroke(color=colors[0],width=5, opacity=1)for i in range(len(pts)-1)])
    
    def addSubLines(buffer, lines, c):  
      for i in range(buffer, len(lines)-1):
        l = Line(lines[i].get_midpoint(), lines[i+1].get_midpoint())
        lines.add(l)
        l.add_updater(lambda mob, i=i : mob.become(Line(lines[i].point_from_proportion(t.get_value()), lines[i+1].point_from_proportion(t.get_value())).set_stroke(color=colors[c],width=5, opacity=1)), True)
        buffer+=1
      if len(lines) < (len(pts) - 1) * (len(pts) / 2):
        addSubLines(buffer + 1, lines, c+1)
    # Recursively make and add lines
    addSubLines(0, lines, 1)
    for i in range(len(lines) - 1):
      d = Dot(lines[i].get_midpoint()).set_fill(color=colors[1+ int(i / (len(pts)-1))])
      points.add(d)
      d.add_updater(lambda mob, i=i : mob.move_to(lines[i].point_from_proportion(t.get_value())))
    
    tracer = Dot(points[0].get_center(), radius=0.1)
    tracer.add_updater(lambda mob : mob.move_to(lines[len(lines)-1].point_from_proportion(t.get_value())))
    points.add(tracer)
    curve = VMobject().set_stroke(width=5)
    curve.set_points_as_corners([points[0].get_center(), points[0].get_center()])
    def update_path(path):
        previous_path = path.copy()
        previous_path.add_points_as_corners([tracer.get_center()])
        path.become(previous_path)
    curve.add_updater(update_path)
  def construct(self):



class Main(AnimatedBezier):
  def construct(self):
    b = AnimatedBezier(pts=[[-2, -2, 0], [0, 3, 0], [3, -3, 0]])
    self.create_bezier_lines()
    self.add(lines, curve, points)
    self.play(t.animate.set_value(1), run_time=3)