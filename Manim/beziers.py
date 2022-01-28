from manim import *
config.pixel_width = 1000
config.pixel_height = 1000
config.frame_height = 10
config.frame_width = 10
config.frame_rate = 60
config.background_color = "#0E1B24"
class Main(Scene):
  def construct(self):
    pts = np.array([
      [-2, -3, 0],
      [-3, 1, 0],
      [0, 3, 0],
      [3, 1, 0],
      [2, -3, 0],
    ])
    colors = ["#ef476f", "#ffd166", "#06d6a0", "#118ab2"]
    t = ValueTracker(0)
    points = VGroup(*[Dot(i, radius=0.1).set_fill(color=config.background_color).set_stroke(WHITE, 3, 1)for i in pts]) 
    points[0].set_fill(color=WHITE)
    lines = VGroup(*[Line(pts[i], pts[i+1]).set_stroke(width=5, opacity=1)for i in range(len(pts)-1)])
    
    def addSubLines(buffer, lines, c):  
      for i in range(buffer, len(lines)-1):
        l = Line(lines[i].get_midpoint(), lines[i+1].get_midpoint())
        lines.add(l)
        l.add_updater(lambda mob, i=i : mob.become(Line(lines[i].point_from_proportion(t.get_value()), lines[i+1].point_from_proportion(t.get_value())).set_stroke(color=colors[c],width=5, opacity=1)), True)
        buffer+=1
      if len(lines) < (len(pts) - 1) * (len(pts) / 2):
        addSubLines(buffer + 1, lines, c+1)
    
    addSubLines(0, lines, 0)
    for i in range(len(lines) - 1):
      d = Dot(lines[i].get_midpoint()).set_fill(color=colors[int(i / (len(pts)-1))])
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

    self.add(lines, curve, points)
    self.play(t.animate.set_value(1), run_time=3)
    

    
    

