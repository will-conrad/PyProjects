from manim import *
from manim_physics import *
from random import *

config.pixel_width = 1000
config.pixel_height = 1000
config.frame_rate = 120

config.background_color = WHITE
box_color = WHITE
objects = 20

class TwoObjectsFalling(SpaceScene): 
    def construct(self):
        
        def get_random_color():
            # colors = ["264653","2a9d8f","e9c46a","f4a261","e76f51"]
            # colors = ["bee9e8","62b6cb","1b4965","cae9ff","5fa8d3"]
            # colors = ["001219","005f73","0a9396","94d2bd","ee9b00","ca6702","bb3e03","ae2012","9b2226"]
            # colors = ["00111c","001523","001a2c","002137","00253e","002945","002e4e","003356","003a61","00406c"]
            colors = ["03045e","023e8a","0077b6","0096c7","00b4d8","48cae4","90e0ef","ade8f4","caf0f8"]

            return "#" + colors[int(random() * len(colors))]
            
        def random_circle():
            # rad = random() * 1.1 + 0.3
            rad = random() * 0.5 + 0.1

            x = random() * 10 - 5
            x + rad + 0.7 if x < 0 else x - rad - 0.7

            y = random() * 20 + 6

            circ = Circle(radius=rad).set_x(x).set_y(y).set_fill(get_random_color(), 1).set_stroke(opacity=0)
            self.make_rigid_body(circ, elasticity=0.6, friction=0.2, density=0.01) 
            return circ

        ground = Line([-5, -5, 0], [5, -5, 0]).set_stroke(color=box_color)
        top = Line([-5, 5, 0], [5, 5, 0]).set_stroke(color=box_color)
        wallL = Line([-5, -5, 0], [-5, 5, 0]).set_stroke(color=box_color)
        wallLHigh = Line([-5, 5, 0], [-5, 40, 0]).set_stroke(opacity=0)
        wallR = Line([5, -5, 0], [5, 5, 0]).set_stroke(color=box_color)
        wallRHigh = Line([5, 5, 0], [5, 40, 0]).set_stroke(opacity=0)
        
        topBox = Rectangle(height = 4, width = 15).set_y(7).set_fill(config.background_color, 1).set_stroke(opacity=0)
        walls = VGroup(ground, wallL, wallR, wallLHigh, wallRHigh)
        self.add(walls)
        
        self.make_static_body(walls)  # Mobjects will stay in place
        
       
        for i in range(200):
            self.add(random_circle())
            
            self.add(topBox, top)
            self.wait(random() * 0.1)
        
        
        self.wait(5)
        cover = Square(10).set_fill(config.background_color, 0).set_stroke(color=config.background_color)
        self.add(cover)
        
        self.play(
            cover.animate.set_opacity(1)
        )



        
        # during wait time, the circle and rect would move according to the simulate updater