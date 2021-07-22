from manim import *
import numpy as np
class Main(Scene):
	def construct(self):
		scale = 1.5

		formula1 = MathTex("a", "x", "^{2}", "+", "b", "x", "+", "c", "=", "0").scale(scale)
		formula2 = MathTex("a", "x", "^{2}", "+", "b", "x", "=", "-", "c").scale(scale)
		formula3 = MathTex("x", "^{2}", "+", "{b", "x", "\\over", "a}", "=", "-", "{c", "\\over", "a}").scale(scale)
		shiftx   = MathTex("x", "^{2}", "+", "{b", "\\over", "a}", "x", "=", "-", "{c", "\\over", "a}").scale(scale)
		formula4 = MathTex("x", "^{2}", "+", "{b", "\\over", "a}", "x", "+", "{b", "^{2}", "\\over", "4", "a", "^{2}}", "=", "-", "{c", "\\over", "a}", "+", "{b", "^{2}", "\\over", "4", "a", "^{2}}").scale(scale)
		complete_square1 = MathTex("{b", "\\over", "a}", "\\times", "{1", "\\over", "2}", "=", "{b", "\\over", "2", "a}").scale(scale)
		complete_square2 = MathTex("\\left(", "{b", "\\over", "2", "a}", "\\right)", "^{2}", "=", "{b", "^{2}", "\\over", "4", "a", "^{2}}").scale(scale)
		formula5 = MathTex("\\left(", "x", "+", "{b", "\\over", "2", "a}", "\\right)", "^{2}", "=", "-", "{c", "\\over", "a}", "+", "{b", "^{2}", "\\over", "4", "a", "^{2}}").scale(scale)
		commonden = MathTex("\\left(", "x", "+", "{b", "\\over", "2", "a}", "\\right)", "^{2}", "=", "-", "{4", "a", "c", "\\over", "4", "a", "^{2}}", "+", "{b", "^{2}", "\\over", "4", "a", "^{2}}").scale(scale)
		formula6 = MathTex("\\left(", "x", "+", "{b", "\\over", "2", "a}", "\\right)", "^{2}", "=", "{b", "^{2}", "-", "4", "a", "c", "\\over", "4", "a", "^{2}}").scale(scale)
		formula7 = MathTex("\\sqrt{", "\\left(", "x", "+", "{b", "\\over", "2", "a}", "\\right)", "^{2}}", "=", "\\sqrt{", "{b", "^{2}", "-", "4", "a", "c", "\\over", "4", "a", "^{2}", "}}").scale(scale)
		splitsqrt= MathTex("\\sqrt{", "\\left(", "x", "+", "{b", "\\over", "2", "a}", "\\right)", "^{2}}", "=", "{", "\\sqrt{", "b", "^{2}", "-", "4", "a", "c", "}", "\\over", "\\sqrt{", "4", "a", "^{2}", "}}").scale(scale)
		formula8 = MathTex("x", "+", "{b", "\\over", "2", "a}", "=", "{\\pm", "\\sqrt{", "b", "^{2}", "-", "4", "a", "c}", "\\over", "2", "a}").scale(scale)
		formula9 = MathTex("x", "=", "{\\pm", "\\sqrt{", "b", "^{2}", "-", "4", "a", "c}", "\\over", "2", "a}", "-", "{b", "\\over", "2", "a}").scale(scale)
		formula10 = MathTex("x", "=", "{-", "b", "\\pm", "\\sqrt{", "b", "^{2}", "-", "4", "a", "c}", "\\over", "2", "a", "}").scale(scale)
		changes = [
			[(0, 1, 2, 3, 4, 5, 6, 7, 8), (0, 1, 2, 3, 4, 5, 7, 8, 6)],

			[(1, 2, 3, 4, 5, 6, 7, 8), (0, 1, 2, 3, 4, 7, 8, 9)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), (0, 1, 2, 3, 6, 4, 5, 7, 8, 9, 10, 11)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), (0, 1, 2, 3, 4, 5, 6, 14,15,16,17, 18)],

			[(3, 4, 5), (0, 1, 2)],

			[(8, 9, 10, 11), (1, 2, 3,  4)],

			[(0, 1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25), (1, 8, 2, 2, 3, 8,  4,  5,  6,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 16, 18, 19, 20, 21, 24)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,20, 21, 22, 23, 24),
			 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19,11, 16, 17, 18, 19)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12, 13, 14, 15, 16, 17, 18, 19, 20, 21)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21), 
			 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24)],

			[(2, 3, 4, 5, 6, 7, 10, 12, 13, 14, 15, 16, 17, 18, 20,22,23),
			 (0, 1, 2, 3, 4, 5, 6,  8,  9, 10, 11, 12, 13, 14, 15,16,17)]

		]

		self.play(
			Write(formula1)
		)
		self.wait(1)

		self.play(*[
			ReplacementTransform(formula1[x], formula2[y])
			for x, y in zip(changes[0][0], changes[0][1])], 
			FadeOut(formula1[9]),
			run_time=2
		)
		self.wait(0.5)
		grid = NumberPlane()
		self.add(grid)

		temp2 = formula2[0].copy()
		# Divide by a
		self.play(*[
			ReplacementTransform(formula2[x], formula3[y])
			for x, y in zip(changes[1][0], changes[1][1])], 
			CounterclockwiseTransform(temp2, formula3[6], path_arc=PI/2),
			CounterclockwiseTransform(formula2[0], formula3[11], path_arc=PI/2),

			# GrowFromCenter(formula3[5]),
			# GrowFromCenter(formula3[10]),
			Create(formula3[5]),
			Create(formula3[10]),
			run_time=2
		)
		self.remove(temp2, formula2[0])
		self.add(formula3)
		self.wait(0.5)

		self.play(*[
			ReplacementTransform(formula3[x], shiftx[y])
			for x, y in zip(changes[2][0], changes[2][1])], 
			
			run_time=1.5
		)
		self.wait(0.5)
		# formula4.shift(UP * 0.03)
		formula4.shift(UP * 1.5)

		# ShiftX (3) to 4 (Partial) / Move Up
		self.play(*[
			ReplacementTransform(shiftx[x], formula4[y])
			for x, y in zip(changes[3][0], changes[3][1])], 
	
			run_time=1.5
		)
		self.wait(0.5)

		coef = VGroup(formula4[3], formula4[4], formula4[5])
		box = SurroundingRectangle(coef)
		self.play(
			Create(box),
			run_time=1.5
		)
		self.wait(0.25)
		complete_square1.shift(DOWN * 1.5)
		complete_square2.shift(DOWN * 1.5)

		self.play(*[
			ReplacementTransform(formula4[x].copy(), complete_square1[y])
			for x, y in zip(changes[4][0], changes[4][1])], 
			
			FadeOut(box),
			run_time=1.5
		)

		self.play(
			Write(complete_square1[3:7]))

		self.wait(0.2)

		self.play(
			Write(complete_square1[7]))

		self.play(
			ReplacementTransform(complete_square1[0].copy(), complete_square1[8]),
			ReplacementTransform(complete_square1[2].copy(), complete_square1[11]),
			ReplacementTransform(complete_square1[6].copy(), complete_square1[10]),
			ReplacementTransform(complete_square1[1].copy(), complete_square1[9]),
			ReplacementTransform(complete_square1[5].copy(), complete_square1[9]),
	
			run_time=1.5
		)

		self.wait(1)


		self.play(*[
			ReplacementTransform(complete_square1[x], complete_square2[y])
			for x, y in zip(changes[5][0], changes[5][1])], 
			FadeOut(complete_square1[0:8]),
			run_time=1.5
		)
		self.wait(0.2)

		self.play(
			FadeIn(complete_square2[0]),
			FadeIn(complete_square2[5]),
			FadeIn(complete_square2[6]),
			run_time=1
		)
		self.play(
			Write(complete_square2[7])
		)



		self.play(
			ReplacementTransform(complete_square2[1].copy(), complete_square2[8]),
			ReplacementTransform(complete_square2[6].copy(), complete_square2[9]),
			ReplacementTransform(complete_square2[3].copy(), complete_square2[11]),
			ReplacementTransform(complete_square2[4].copy(), complete_square2[12]),
			ReplacementTransform(complete_square2[6].copy(), complete_square2[13]),
			ReplacementTransform(complete_square2[2].copy(), complete_square2[10]),
	
			run_time=1.5
		)
		self.wait(1.5)

		self.play(
			ReplacementTransform(complete_square2[8].copy(), formula4[8]),
			ReplacementTransform(complete_square2[9].copy(), formula4[9]),
			ReplacementTransform(complete_square2[10].copy(), formula4[10]),
			ReplacementTransform(complete_square2[11].copy(), formula4[11]),
			ReplacementTransform(complete_square2[12].copy(), formula4[12]),
			ReplacementTransform(complete_square2[13].copy(), formula4[13]),

			ReplacementTransform(complete_square2[8], formula4[20]),
			ReplacementTransform(complete_square2[9], formula4[21]),
			ReplacementTransform(complete_square2[10], formula4[22]),
			ReplacementTransform(complete_square2[11], formula4[23]),
			ReplacementTransform(complete_square2[12], formula4[24]),
			ReplacementTransform(complete_square2[13], formula4[25]),

			FadeOut(complete_square2[0:8]),
			Write(formula4[7]),
			Write(formula4[19]),
			
			run_time=2
		)
		self.wait(0.5)

		self.play(
			formula4.animate.shift(DOWN*1.5),
			run_time=1
		)

		self.wait(0.5)

		self.play(*[
			ReplacementTransform(formula4[x], formula5[y])
			for x, y in zip(changes[6][0], changes[6][1])], 
			FadeOut(formula4[3:7]),
			GrowFromCenter(formula5[0]),
			GrowFromCenter(formula5[7]),
			run_time=2.5
		)
		self.wait(1)
		
		self.play(*[
			ReplacementTransform(formula5[x], commonden[y])
			for x, y in zip(changes[7][0], changes[7][1])], 
			ReplacementTransform(formula5[18].copy(), commonden[11]),
			ReplacementTransform(formula5[18].copy(), commonden[15]),
			ReplacementTransform(formula5[18], commonden[22]),
			ReplacementTransform(formula5[19].copy(), commonden[12]),
			ReplacementTransform(formula5[19].copy(), commonden[12]),
			ReplacementTransform(formula5[19].copy(), commonden[16]),
			ReplacementTransform(formula5[19], commonden[23]),
			Write(commonden[17]),
			run_time=2
		)


		self.wait(1)
		self.play(*[
			ReplacementTransform(commonden[x], formula6[y])
			for x, y in zip(changes[8][0], changes[8][1])],
			CounterclockwiseTransform(commonden[19], formula6[10], path_arc=PI/2),
			CounterclockwiseTransform(commonden[20], formula6[11], path_arc=PI/2),
			FadeOut(commonden[18]),
			run_time=2
		)
		self.remove(commonden[19], commonden[20])
		self.add(formula6)

		self.wait(0.5)
		dummy = VMobject()
		sqrts = VGroup(formula7[0], formula7[11])
		self.play(*[
			ReplacementTransform(formula6[x], formula7[y])
			for x, y in zip(changes[9][0], changes[9][1])], 
			LaggedStart(dummy.animate.shift(UP), Write(sqrts), lag_ratio=0.7),
			run_time=2
		)

		

		self.play(*[
			ReplacementTransform(formula7[x], splitsqrt[y])
			for x, y in zip(changes[10][0], changes[10][1])], 

			ReplacementTransform(formula7[11].copy(), splitsqrt[12]),
			ReplacementTransform(formula7[11], splitsqrt[21]),
	
			# ReplacementTransform(formula7[22], splitsqrt[23]),
			# formula7[0].animate.set_color(RED),
			run_time=2

		)
		self.wait(0.8)
		blink = VGroup(splitsqrt[0], splitsqrt[9], splitsqrt[21], splitsqrt[22], splitsqrt[24])

		self.play(
			blink.animate.set_color(RED),
			run_time=0.8)
		self.wait(0.5)

		formula8[7].shift(RIGHT*1.05)
		
		lpar_temp = splitsqrt[1].copy().set_opacity(0)
		rpar_temp = splitsqrt[8].copy().set_opacity(0)
		lroot_temp = splitsqrt[0].copy().set_opacity(0)
		lsqr_temp = splitsqrt[9].copy().set_opacity(0)
		
		roottemp = splitsqrt[21].copy().set_opacity(0)
		sqr_temp = splitsqrt[24].copy().set_opacity(0)

		lpar_temp.shift(LEFT*0.25)
		rpar_temp.shift(LEFT*0.55)
		lroot_temp.shift(LEFT*0.25)
		lsqr_temp.shift(LEFT*0.25)
		roottemp.shift(LEFT*1.2)
		sqr_temp.shift(LEFT*1.2)
		
		
		self.play(*[
			ReplacementTransform(splitsqrt[x], formula8[y])
			for x, y in zip(changes[11][0], changes[11][1])],
			
			
			Write(formula8[7]),
			formula8[7].animate.shift(LEFT),
			
			ReplacementTransform(splitsqrt[21], roottemp),
			ReplacementTransform(splitsqrt[24], sqr_temp),
			
			ReplacementTransform(splitsqrt[1], lpar_temp),
			ReplacementTransform(splitsqrt[8], rpar_temp),
			ReplacementTransform(splitsqrt[0], lroot_temp),
			ReplacementTransform(splitsqrt[9], lsqr_temp),

			run_time=2
		)
		self.add(formula8)
		self.remove(lsqr_temp, lroot_temp, rpar_temp, lpar_temp, roottemp, sqr_temp)



		



class Test(Scene):
	def construct(self):
		a = MathTex("x", "_1")
		b = MathTex("y", "_1")
		self.add(a)
		self.wait()
		a = b
		self.add(a)
		self.wait()

		



def vdw(Tr, Vr):
	pr = 8 * Tr / (3 * Vr - 1) - 3 / Vr * 2
	return pr
class Example(ThreeDScene):
	

    def construct(self):
    	

        # self.camera.background_color = "#ece6e2"
        resolution_fa = 42
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

       

        def gauss2(u,v):
            return np.array([u, v, vdw(u,v)/10])

        gauss_plane = ParametricSurface(
            gauss2,
            resolution=(resolution_fa, resolution_fa),
          
            v_min=1,
            v_max=10,
            
            u_min=1,
            u_max=10
        )

        gauss_plane.set_style(fill_opacity=1,stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)
        gauss_plane.move_to(ORIGIN)
        axes = ThreeDAxes()
        self.add(axes,gauss_plane)
# (8, 9, 10, 11), (1, 2, 3, 4)
# (0"{b", 1"\\over", 2"a}", 3"\\times", 4"{1", 5"\\over", 6"2}", 7"=", 8"{b", 9"\\over", 10"2", 11"a}").scale(scale)
#8"{b", 9"^{2}", 10"\\over", 11"4", 12"a", 13"^{2}}"

#20"{b", 21"^{2}", 22"\\over", 23"4", 24"a", 25"^{2}}")
		




