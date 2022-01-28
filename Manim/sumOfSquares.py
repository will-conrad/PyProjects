from manim import *
from colorsys import *

config.pixel_width = 500
config.pixel_height = 500
config.frame_height = 5
config.frame_width = 5

class Main(Scene):
  def construct(self):
    def getColor(hue):
      return rgb_to_color(hsv_to_rgb(hue, 0.7, 1))
    
    self.hue = 0
    self.width = 1
    self.scale = 1.5
    self.increment = 0.05
    self.exp = 1
    rect = np.array([
      [-2, 2, 0],
      [2, 2, 0],
      [2, -2, 0],
      [-2, -2, 0]  
    ])
    self.add(
      Polygon(*rect).set_fill(getColor(self.hue), opacity=1).set_stroke(color=WHITE, width=self.width)
    )
    def rectOver(rect):
      width = rect[1, 0] - rect[0, 0]
      newRect = np.array([
        rect[0],
        [rect[1, 0]- width/2, rect[0, 1], 0], 
        [rect[1, 0]- width/2, rect[2, 1], 0],
        rect[3]
      ])
      
      self.add(MathTex("1", "\\over", pow(2, self.exp)).scale(self.scale * 1.25).move_to(Polygon(*newRect).get_center()).shift(RIGHT * (width/2)))
      self.play(
        Transform(
          Polygon(*rect).set_fill(getColor(self.hue), opacity=1).set_stroke(color=WHITE, width=self.width), 
          Polygon(*newRect).set_fill(getColor(self.hue + self.increment), opacity=1).set_stroke(color=WHITE, width=self.width))
      )
      
      self.hue += self.increment
      self.exp += 1
      return newRect

    def rectDown(rect):
      height = rect[0, 1] - rect[2, 1]
      newRect = np.array([
        [rect[0, 0], rect[2, 1] + height/2, 0],
        [rect[2, 0], rect[3, 1] + height/2, 0], 
        rect[2],
        rect[3]
      ])
      self.add(MathTex("1", "\\over", pow(2, self.exp)).scale(self.scale).move_to(Polygon(*newRect).get_center()).shift(UP * (height/2)))
      
      self.play(
        Transform(
          Polygon(*rect).set_fill(getColor(self.hue), opacity=1).set_stroke(color=WHITE, width=self.width), 
          Polygon(*newRect).set_fill(getColor(self.hue + self.increment), opacity=1).set_stroke(color=WHITE, width=self.width)
        )
      )
      self.scale /= 2
      self.hue += self.increment
      self.exp += 1
      return newRect
    # max = 8
    for i in range(8):
      rect = rectOver(rect)
      rect  = rectDown(rect)