from manim import *
from math import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30

OVER_LEFT = LEFT * config.frame_width
OVER_RIGHT = RIGHT * config.frame_width
WIDTH = config.frame_width

def set_angle(self, angle, about_point=None):
  if about_point is None:
      about_point = self.get_start()
  self.rotate(
      angle - self.get_angle(),
      about_point=about_point,
  )
  return self


class TriangleScene(Scene):
  ptA = [0, 7.30951, 0]
  ptB = [-2.5, -6.86869, 0]
  ptC = [2.5, -6.86869, 0]
  ptF = [-1.85557, -3.21393, 0]
  pts = np.array([ptA, ptB, ptC])
  
  ltrA = Tex("A").move_to(ptA).scale(1.75).shift(RIGHT * 0.5, UP * 0.2)
  ltrB = Tex("B").move_to(ptB).scale(1.75).shift(LEFT * 0.5)
  ltrC = Tex("C").move_to(ptC).scale(1.75).shift(RIGHT * 0.5)
  ltrF = Tex("F").move_to(ptF).scale(1.75).shift(LEFT * 0.5)
  letters = VGroup(ltrA, ltrB, ltrC, ltrF)

  lnBC = Line(ptB, ptC)
  lnAC = Line(ptC, ptA)
  lnAB = Line(ptB, ptA)
  lnCF = Line(ptC, ptF)
  lines = VGroup(lnBC, lnAC, lnAB)
  
  triangle = Polygon(*[ptA, ptB, ptC]).set_stroke(color=WHITE, width=5)

  angA = Angle(lnAB, lnAC, radius=1.5, quadrant=(-1, -1))
  angAText = Tex("20$^\circ$").move_to(ptA).shift(DOWN * 2.4)

  angB = Angle(lnAB, lnBC, radius=1, quadrant=(1, 1), other_angle=True)
  angB_buff = Angle(lnAB, lnBC, radius=1.5, quadrant=(1, 1), other_angle=True)

  angC = Angle(lnAC, lnBC, radius=1, quadrant=(1, -1), other_angle=False)
  angC_buff = Angle(lnAC, lnBC, radius=1.5, quadrant=(1, -1), other_angle=False)
  
  angF = Angle(lnAC, lnCF, radius=2, quadrant=(1, -1), other_angle=False)
  angF_buff = Angle(lnAC, lnBC, radius=2.5, quadrant=(1, -1), other_angle=False)
  
  angles = VGroup(angA, angB, angC, angF)

class ProblemScene(MovingCameraScene):
  t = Tex("The Problem")
  line = Line([-3, 0, 0], [3, 0, 0]).next_to(t, DOWN)
  header = VGroup(t, line).shift(UP*4)
  p1 = Tex("$\\triangle$ABC is an isosceles triangle").arrange(LEFT)
  p2 = Tex("$\\angle{B}$ and $\\angle{C}$ = 80$^{\\circ}$").next_to(p1, DOWN, 0.6, LEFT) 
  p3a = Tex("$\\overline{\\rm{CF}}$ is 30$^{\\circ}$ to $\\overline{\\rm{AC}}$ and intersects $\\overline{\\rm{AB}}$").next_to(p2, DOWN, 0.6, LEFT)
  p3b = Tex("at F").next_to(p3a, DOWN, 0.3, LEFT)
  p4a = Tex("$\\overline{\\rm{BE}}$ is 20$^{\\circ}$ to $\\overline{\\rm{AB}}$ and intersects $\\overline{\\rm{AC}}$").next_to(p3b, DOWN, 0.6, LEFT)
  p4b = Tex("at E").next_to(p4a, DOWN, 0.3, LEFT)
  p5 = Tex("Find $\\angle{BEF}$").next_to(p4b, DOWN, 0.6, LEFT)
  problem = VGroup(p1, p2, p3a, p3b, p4a, p4b, p5).move_to(ORIGIN)
  p1p2_scale = 1.25
  p3p4_scale = 1.1

class Title(Scene):
  def construct(self):
    t2 = Tex("Adventitious").scale(2)
    t1 = Tex("Langley's").scale(2).next_to(t2, UP, buff=0.7)
    t3 = Tex("Angles").scale(2).next_to(t2, DOWN, buff=0.7)
    t = VGroup(t1, t2, t3)
    self.play(
      Write(t),
    )
    self.wait()

class Problem(ProblemScene):
  def construct(self):
    header = self.header.shift(DOWN*4)
    self.play(Write(header), run_time=2)
    self.wait(0.5)
    self.play(header.animate.shift(UP*4))
    self.play(
      Write(self.problem),
      run_time=4
    )
    self.wait()  

class P1P2TransitionTO(ProblemScene):
  def construct(self):
    self.add(self.header, self.problem)
    p1 = self.p1
    p2 = self.p2
    text = VGroup(p1, p2)
    box = SurroundingRectangle(text)
    self.play(Create(box))
    self.wait()
    self.play(
      VGroup(text, box).animate.scale(self.p1p2_scale).set_x(0),
      self.problem[2:7].animate.set_opacity(0.6),
      self.header.animate.set_opacity(0.6)
    )
    self.wait()
    self.play(
      self.camera.frame.animate.shift(OVER_RIGHT)
    )
    self.wait()

class P1P2(TriangleScene):
  def construct(self):
    grid = NumberPlane(y_range=[-8, 8]).set_opacity(0.5)
    self.add(grid)

    self.play(Write(self.triangle))
    self.play(
      Write(self.letters),
      Create(self.angles)
    )
    self.wait(1.5)
    
    angBText = Tex(str(80) + "$^\circ$").move_to(self.angB_buff.point_from_proportion(0.5))
    angCText = Tex(str(80) + "$^\circ$").move_to(self.angC_buff.point_from_proportion(0.5))

    self.play(
      Write(angBText),
      Write(angCText)
    )
    eq1 = MathTex("180^\circ")
    eq2 = MathTex("-", "80^\circ").next_to(eq1, DOWN, 0.4).shift(LEFT * 0.07)
    eq3 = MathTex("-", "80^\circ").next_to(eq2, DOWN, 0.4, RIGHT)
    eq4 = MathTex("= ", "20^\circ").next_to(eq3, DOWN, 0.4, RIGHT)
    eq = VGroup(eq1, eq2, eq3, eq4)
    eq.move_to([-2.5, 6, 0])
    self.play(Write(eq[0]))
    self.wait()
    self.play(
      Write(eq[1][0]),
      Write(eq[2][0]),
      ReplacementTransform(angBText.copy(), eq[1][1]),
      ReplacementTransform(angCText.copy(), eq[2][1]),
      run_time=1.5
    )
    self.play(
      Write(eq[3])
    )
    self.wait()
    self.play(
      ReplacementTransform(eq[3].copy(), self.angAText),
      Unwrite(eq)
    )
    self.wait()

class P1P2TransitionFROM(TriangleScene, ProblemScene):
  
  def construct(self):
    header = self.header
    problem = self.problem

    self.add(
      self.triangle,
      self.angles,
      self.letters,
      self.angAText,
      Tex(str(80) + "$^\circ$").move_to(self.angB_buff.point_from_proportion(0.5)),
      Tex(str(80) + "$^\circ$").move_to(self.angC_buff.point_from_proportion(0.5))
    )
    
    header.shift(OVER_LEFT).set_opacity(0.6)
    self.add(header)
    problem.shift(OVER_LEFT)
    problem[0:2].scale(self.p1p2_scale).set_x(WIDTH * -1)
    problem[2:].set_opacity(0.6)
    
    group = VGroup(problem[0:2])
    box = SurroundingRectangle(group)
    self.add(problem, box)

    self.play(
      self.camera.frame.animate.shift(OVER_LEFT)
    )
    
    self.play(
      LaggedStart(
        Unwrite(box),
        AnimationGroup(
          problem.animate.set_opacity(1),
          header.animate.set_opacity(1),
          group.animate.scale(1/self.p1p2_scale).next_to(self.p3a, UP, 0.6, LEFT) 
        ),
        lag_ratio=0.6
      )
    )
    self.wait()
    
class P3P4TransitionTO(ProblemScene, TriangleScene):
  def construct(self):
    header = self.header
    problem = self.problem
    self.add(header, problem)
    p3a = self.p3a
    p3b = self.p3b
    p4a = self.p4a
    p4b = self.p4b
    text = VGroup(p3a, p3b, p4a, p4b)
    box = SurroundingRectangle(text)
    self.play(Create(box), run_time=1)
    self.wait()
    self.play(
      VGroup(text, box).animate.scale(self.p3p4_scale).set_x(0),
      problem[0:2].animate.set_opacity(0.6),
      problem[6].animate.set_opacity(0.6),
      header.animate.set_opacity(0.6)
    )
    
    shift_group = VGroup(
      self.triangle,
      self.angles,
      self.letters,
      self.angAText,
      Tex(str(80) + "$^\circ$").move_to(self.angB_buff.point_from_proportion(0.5)),
      Tex(str(80) + "$^\circ$").move_to(self.angC_buff.point_from_proportion(0.5)),
    ).shift(OVER_RIGHT)
    self.add(shift_group)
    self.wait()
    self.play(
      self.camera.frame.animate.shift(OVER_RIGHT)
    )
    self.wait()


class P3P4(TriangleScene, MovingCameraScene):
  def construct(self):
    grid = NumberPlane(y_range=[-8, 8]).set_opacity(0.5)
    c1 = ValueTracker(80)
    c2 = ValueTracker(100)
    c_ang1_prop = ValueTracker(0.5)
    c_ang2_prop = ValueTracker(1)
    
    eightyDeg = Tex("80$^\circ$")
    
    self.add(
      grid,
      self.triangle,
      self.angles,
      self.letters,
      self.angAText,
      Tex(str(80) + "$^\circ$").move_to(self.angB_buff.point_from_proportion(0.5)),
      eightyDeg,
    )
    eightyDeg.add_updater(lambda a : a.move_to(self.angC_buff.point_from_proportion(c_ang1_prop.get_value())))
    self.ltrF.set_opacity(0).move_to(self.ptA)
    self.wait()
    self.play(self.ltrC.animate.set_color(YELLOW))
    self.play(
      Create(self.lnAC.set_color(YELLOW))
    )
    mv_line = self.lnAC
    mv_line_vis = self.lnAC
    lnAB = self.lnAB
    mv_line.add_updater(lambda l : l.set_angle(c2.get_value() * DEGREES, about_point=self.ptC))
    mv_line_vis.add_updater(lambda l : l.set_angle(c2.get_value() * DEGREES, about_point=self.ptC).become(Line(self.ptC, line_intersection((l.get_start(), l.get_end()), (lnAB.get_start(), lnAB.get_end()))).set_color(YELLOW)))
    ptF = Point(color=WHITE).add_updater(lambda p : p.move_to(line_intersection((mv_line_vis.get_start(), mv_line_vis.get_end()), (lnAB.get_start(), lnAB.get_end()))))
    self.ltrF.add_updater(lambda l : l.move_to(ptF).shift(LEFT * 0.5))
    self.add(ptF)
    self.add(mv_line_vis, mv_line)
    
    self.angC.add_updater(lambda a : a.become(Angle(mv_line, self.lnBC, radius=1, quadrant=(1, -1), other_angle=False)))
    self.angF.add_updater(lambda f : f.become(Angle(self.lnAB, mv_line, quadrant=(1, -1), radius=2)))
    
    self.play(
      c1.animate.set_value(50),
      c2.animate.set_value(140),
      self.ltrF.animate.set_opacity(1),
      c_ang1_prop.animate.set_value(0.75),
      
      run_time=5)
    self.wait()