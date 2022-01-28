from turtle import up
from manim import *
config.pixel_width = 1000
config.pixel_height = 1000
config.frame_height = 10
config.frame_width = 10
class Lissajous(Scene):
    
    def lissajous(self):
        circleSize = 1.25
        buffer = 1.5
        self.upAngle = ValueTracker(0)
        self.sideAngle = ValueTracker(0)
        grid = NumberPlane([-5, 5, 1], [-5, 5, 1]).set_opacity(0.5)
        self.add(grid)
        
        upperCircle = Circle(circleSize).shift(UP * (config.frame_height/2 - buffer)).set_fill(opacity=0)
        upperDot = Dot().move_to(upperCircle.point_from_proportion(self.upAngle.get_value()%1))
        self.add(upperCircle, upperDot)

        sideCircle = Circle(circleSize).shift(LEFT * (config.frame_width / 2 - buffer)).set_fill(opacity=0)
        sideDot = Dot().move_to(sideCircle.point_from_proportion(self.sideAngle.get_value()%1))
        self.add(sideCircle, sideDot)
        

        
    
        upperDot.add_updater(lambda x: x.move_to(upperCircle.point_from_proportion(self.upAngle.get_value()%1)))
        sideDot.add_updater(lambda x: x.move_to(sideCircle.point_from_proportion(self.sideAngle.get_value()%1)))

        intersection = Dot([upperDot.get_x(), sideDot.get_y(), 0])
        intersection.add_updater(lambda z: z.become(Dot([upperDot.get_x(), sideDot.get_y(), 0])))
        self.add(intersection)
        
        curve = VMobject()
        curve.set_points_as_corners([intersection.get_center(), intersection.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([intersection.get_center()])
            path.become(previous_path)
        curve.add_updater(update_path)
        self.add(curve)
        
        vLine = Line(upperDot.get_center(), intersection.get_center())
        hLine = Line(sideDot.get_center(), intersection.get_center())
        vLine.add_updater(lambda v: v.become(Line(upperDot.get_center(), [upperDot.get_x(), sideDot.get_y(), 0])))
        hLine.add_updater(lambda h: h.become(Line(sideDot.get_center(), [upperDot.get_x(), sideDot.get_y(), 0])))
        self.add(vLine, hLine)
        # pointX = ValueTracker(upperDot.get_x())
        # pointY = ValueTracker(sideDot.get_y())
        self.play(
            self.upAngle.animate(rate_func=linear).set_value(3),
            self.sideAngle.animate(rate_func=linear).set_value(4), 
            run_time=6
        )
    def construct(self):
        self.lissajous()

        


    

