from manim import *
config.pixel_width = 500
config.pixel_height = 500
class Lissajous(Scene):
    
    def construct(self):
        nCircle = Circle(1.5).set_fill(opacity=0).shift(UP * 4.5)
        wCircle = Circle(1.5).set_fill(opacity=0).shift(LEFT * 4.5)
        self.add(nCircle, wCircle)
        nDot = Dot(radius=0.08, color=YELLOW)
        wDot = Dot(radius=0.08, color=YELLOW)
        self.add(nDot, wDot)
        nDot.move_to(nCircle.point_from_proportion(0))
        wDot.move_to(nCircle.point_from_proportion(0))
        nRate = 0.25
        wRate = 0.25
        self.nOffset = 0
        self.wOffset = 0

        def go_around_top_circle(mob, dt):
            
            self.offset += rate *  dt
            # print(self.t_offset)
            mob.move_to(circle.point_from_proportion(self.offset % 1))
        
        def go_around_top_circle(mob, dt):
            self.offset += rate *  dt
            # print(self.t_offset)
            mob.move_to(circle.point_from_proportion(self.offset % 1))
        def get_line_to_circle():
            return Line([0, 0, 0], dot.get_center(), color=BLUE)
        
        def get_line_to_down():
            return Line([dot.get_x(), -1 * config.frame_height, 0], dot.get_center(), color=BLUE)
        
        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        bottom_to_dot = always_redraw(get_line_to_down)
        self.add(bottom_to_dot)
        self.wait(4)

        