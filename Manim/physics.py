from manim import *
from manim_physics import *
from random import *

config.pixel_width = 1000
config.pixel_height = 1000
config.frame_rate = 60
config.background_color = WHITE

box_color = WHITE
box_weight = 0.15
objects = 20

class TwoObjectsFalling(SpaceScene):
    

    def construct(self):
        def get_random_color():
            # colors = ["264653","2a9d8f","e9c46a","f4a261","e76f51"]
            colors = ["bee9e8","62b6cb","1b4965","cae9ff","5fa8d3"]
            
            return "#" + colors[int(random() * len(colors))]
            
        def random_circle():
            rad = random() * 1.2 + 0.3

            x = random() * 10 - 5
            x + rad + 0.7 if x < 0 else x - rad - 0.7

            y = random() * 10 + 6

            circ = Circle(radius=rad).set_x(x).set_y(y).set_fill(get_random_color(), 1).set_stroke(opacity=0)
            self.make_rigid_body(circ, elasticity=0.6, friction=0) 
            return circ

        
        

        ground = Line([-5, -5, 0], [5, -5, 0]).set_stroke(color=box_color)
        top = Line([-5, 5, 0], [5, 5, 0]).set_stroke(color=box_color)
        wallL = Line([-5, -5, 0], [-5, 5, 0]).set_stroke(color=box_color)
        wallLHigh = Line([-5, 5, 0], [-5, 15, 0]).set_stroke(opacity=0)
        wallR = Line([5, -5, 0], [5, 5, 0]).set_stroke(color=box_color)
        wallRHigh = Line([5, 5, 0], [5, 15, 0]).set_stroke(opacity=0)
        
        topBox = Rectangle(height = 4, width = 15).set_y(7).set_fill(config.background_color, 1).set_stroke(opacity=0)
        # pusher = Rectangle(height = 3, width = 9.98).set_y(15).set_fill(BLACK, 0)
        walls = VGroup(ground, wallL, wallR, wallLHigh, wallRHigh)
        self.add(walls)
        
        self.make_static_body(walls)  # Mobjects will stay in place
        for i in range(40):
            self.add(random_circle())
            self.add(topBox, top)
            self.wait(random() * 0.5)
        # self.make_rigid_body(pusher, density=200, friction=0, elasticity=0)
        
        self.wait(1.5)
        # self.remove(ground)
        # self.wait(3)
        cover = Square(10).set_fill(WHITE, 0)
        self.add(cover)
        self.play(
            cover.animate.set_opacity(1)
        )


        
        # during wait time, the circle and rect would move according to the simulate updater