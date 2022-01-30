from manim import *
config.pixel_width = 500
config.pixel_height = 500
config.frame_height = 10
config.frame_width = 10
config.frame_rate = 30
config.background_color = "#0E1B24"
    
class AnimatedBezierScene(Scene):
  def construct(self):
    pts = np.array([
      [-3.5, -4, 0],
      [-3.5, 1, 0],
      [0, 2.6, 0],
      [0, -2.6, 0],
      [3.5, -1, 0],
      [3.5, 4, 0]
    ])
    colors = ["#ef476f", "#ffd166", "#06d6a0", "#118ab2", "#118ab2"]
    t = ValueTracker(0)
    points = VGroup(*[Dot(i, radius=0.1).set_fill(color=config.background_color).set_stroke(WHITE, 3, 1)for i in pts]) 
    points[0].set_fill(color=WHITE)
    for p in points:
      p.add_updater(lambda mob : mob.set_z())
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
      d = Dot(radius=0.09, point=lines[i].get_midpoint()).set_fill(color=colors[int(i / (len(pts)-1))])
      points.add(d)
      d.add_updater(lambda mob, i=i : mob.move_to(lines[i].point_from_proportion(t.get_value())))
    
    tracer = Dot(points[0].get_center(), radius=0.1)
    tracer.add_updater(lambda mob : mob.move_to(lines[len(lines)-1].point_from_proportion(t.get_value())))
    points.add(tracer)
    curve = VMobject().set_stroke(width=7)
    curve.set_points_as_corners([points[0].get_center(), points[0].get_center()])
    def update_path(path):
        previous_path = path.copy()
        previous_path.add_points_as_corners([tracer.get_center()])
        path.become(previous_path)
    curve.add_updater(update_path)

    self.add(lines, points, curve)
    self.play(t.animate.set_value(1), run_time=4)
    self.wait()