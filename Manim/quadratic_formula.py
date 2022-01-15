from manim import *

class Main(Scene):
	def construct(self):
		scale = 1.5
		# All of the different formulas broken down so each element has a unique index
		# This makes transforming many things at once tedious but straightforward

		#This proof was interpreted from this image: https://i.pinimg.com/originals/51/a0/92/51a09239ad0e6d0d660d839f900f077a.png
		formula = MathTex("a", "x", "^{2}", "+", "b", "x", "+", "c", "=", "0").scale(scale)
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
		
		# List that describes how each index of one formula transforms to the right index in the subsequent formula
		changes = [
			[(0, 1, 2, 3, 4, 5, 6, 7, 8),
			 (0, 1, 2, 3, 4, 5, 7, 8, 6)],

			[(1, 2, 3, 4, 5, 6, 7, 8),
			 (0, 1, 2, 3, 4, 7, 8, 9)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11),
			 (0, 1, 2, 3, 6, 4, 5, 7, 8, 9, 10, 11)],

			[(0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11),
			 (0, 1, 2, 3, 4, 5, 6, 14, 15, 16, 17, 18)],

			[(3, 4, 5),
			 (0, 1, 2)],

			[(8, 9, 10, 11),
			 (1, 2, 3,  4)],

			[(0, 1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25),
			 (1, 8, 2, 2, 3, 8,  4,  5,  6,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20),
			 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 16, 18, 19, 20, 21, 24)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24),
			 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 11, 16, 17, 18, 19)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19),
			 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21), 
			 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 20, 22, 23, 24)],

			[(2, 3, 4, 5, 6, 7, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23),
			 (0, 1, 2, 3, 4, 5, 6,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17)],

			[(0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17),
			 (0, 1, 2, 3, 4, 5,  6,  7,  8,  9,  10, 11, 12)],

			[(0, 1, 2, 3, 4, 5, 6, 7, 8,  9,  10, 11, 12, 15, 16, 17),
			 (0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 12, 13, 14)]

		]

		# Write the first formula and wait
		self.play(
			Write(formula1)
		)
		self.wait(1)

		# Subtract both sides by c
		self.play(*[

			# Take each pair of indexes from the first group in the changes list and pass them as the
			# index to transform from and the index to transform to
			ReplacementTransform(formula1[x], formula2[y])
			for x, y in zip(changes[0][0], changes[0][1])], 
			# Fade out 0
			FadeOut(formula1[9]),
			run_time=2
		)

		self.wait(0.5)

		# Divide by a
		# Because one index has to transform into 2 places, create a duplicate first
		temp2 = formula2[0].copy()
		
		self.play(*[
			ReplacementTransform(formula2[x], formula3[y])
			for x, y in zip(changes[1][0], changes[1][1])], 
			# Rotate the duplicate a and the actual a into place
			CounterclockwiseTransform(temp2, formula3[6], path_arc=PI/2),
			CounterclockwiseTransform(formula2[0], formula3[11], path_arc=PI/2),
			# Create the fraction lines
			Create(formula3[5]),
			Create(formula3[10]),
			run_time=2
		)
		# Rotational transforms move element a to element b and transforms to look like element b, but what you see
		# on screen is still element a. 
		# Remove the elements from formula 2 and add in the full formula 3
		self.add(formula3)
		self.remove(temp2, formula2[0])
		
		self.wait(0.5)

		# Shift x from numerator to beside the fraction
		self.play(*[
			ReplacementTransform(formula3[x], shiftx[y])
			for x, y in zip(changes[2][0], changes[2][1])], 
			
			run_time=1.5
		)

		self.wait(0.5)

		# Shift destination formula up to make room for completing the square
		formula4.shift(UP * 1.5)

		# Move formula up and leave room for extra elements to come later
		self.play(*[
			ReplacementTransform(shiftx[x], formula4[y])
			for x, y in zip(changes[3][0], changes[3][1])], 
	
			run_time=1.5
		)

		self.wait(0.5)

		# Coefficient group
		coef = VGroup(formula4[3], formula4[4], formula4[5])
		# Draw a box around the coefficient
		box = SurroundingRectangle(coef)

		self.play(
			Create(box),
			run_time=1.5
		)

		self.wait(0.25)

		# Premptively move later formulas down
		complete_square1.shift(DOWN * 1.5)
		complete_square2.shift(DOWN * 1.5)

		# Move b/a down
		completesquare = Tex("Completing the Square").scale(1.25).shift(DOWN * 3)
		self.play(*[
			ReplacementTransform(formula4[x].copy(), complete_square1[y])
			for x, y in zip(changes[4][0], changes[4][1])], 
			
			FadeOut(box),
			FadeIn(completesquare),
			run_time=1.5
		)
		# return()
		# Add the rest of the equation
		self.play(
			Write(complete_square1[3:7])
		)
		self.wait(0.2)

		# Write =
		self.play(
			Write(complete_square1[7])
		)
		# Move elements across to form the solution
		self.play(
			ReplacementTransform(complete_square1[0].copy(), complete_square1[8]),
			ReplacementTransform(complete_square1[2].copy(), complete_square1[11]),
			ReplacementTransform(complete_square1[6].copy(), complete_square1[10]),
			ReplacementTransform(complete_square1[1].copy(), complete_square1[9]),
			ReplacementTransform(complete_square1[5].copy(), complete_square1[9]),
	
			run_time=1.5
		)

		self.wait(1)

		# Move the solution left and fade out the existing formula
		self.play(*[
			ReplacementTransform(complete_square1[x], complete_square2[y])
			for x, y in zip(changes[5][0], changes[5][1])], 
			FadeOut(complete_square1[0:8]),
			run_time=1.5
		)

		self.wait(0.2)

		# Add ()^2
		self.play(
			FadeIn(complete_square2[0]),
			FadeIn(complete_square2[5]),
			FadeIn(complete_square2[6]),
			run_time=1
		)

		# Add =
		self.play(
			Write(complete_square2[7])
		)


		# Move elements across and distribute the ^2
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

		# Move everything back up
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

			# Fade out bottom formula
			FadeOut(complete_square2[0:8]),
			#Fade out "completing the square"
			FadeOut(completesquare),
			# Add in plus signs
			Write(formula4[7]),
			Write(formula4[19]),
			
			run_time=2
		)
		#return()

		self.wait(0.5)

		# Move everything down
		self.play(
			formula4.animate.shift(DOWN*1.4),
			run_time=1
		)

		self.wait(0.5)

		# Simplify left side
		self.play(*[
			ReplacementTransform(formula4[x], formula5[y])
			for x, y in zip(changes[6][0], changes[6][1])],
			# Fade out middle nomial 
			FadeOut(formula4[3:7]),
			# Add parenthesis
			GrowFromCenter(formula5[0]),
			GrowFromCenter(formula5[7]),
			run_time=2.5
		)

		self.wait(1)
		
		# Right side get common denomonator (4a gets distributed)
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
			# Add ^2
			Write(commonden[17]),
			run_time=2
		)

		self.wait(1)

		# Simplify right side and rearrange numerator
		self.play(*[
			ReplacementTransform(commonden[x], formula6[y])
			for x, y in zip(changes[8][0], changes[8][1])],
			CounterclockwiseTransform(commonden[19], formula6[10], path_arc=PI/2),
			CounterclockwiseTransform(commonden[20], formula6[11], path_arc=PI/2),
			# Remove plus sign
			FadeOut(commonden[18]),
			run_time=2
		)
		self.remove(commonden[19], commonden[20])
		self.add(formula6)

		self.wait(0.5)
		# Dummy is an invisable object that wastes time to delay events 
		dummy = VMobject()
		sqrts = VGroup(formula7[0], formula7[11])
		self.play(*[
			ReplacementTransform(formula6[x], formula7[y])
			for x, y in zip(changes[9][0], changes[9][1])], 
			# Animate dummy to delay, then animate writing the roots
			LaggedStart(dummy.animate.shift(UP), Write(sqrts), lag_ratio=0.7),
			run_time=2
		)

		self.wait(0.75)
		# Splits sqrt into one in numerator and one in demomonator
		self.play(*[
			ReplacementTransform(formula7[x], splitsqrt[y])
			for x, y in zip(changes[10][0], changes[10][1])], 
			ReplacementTransform(formula7[11].copy(), splitsqrt[12]),
			ReplacementTransform(formula7[11], splitsqrt[21]),
	
			run_time=2
		)

		self.wait(0.8)

		# Group of things that cancel each other
		blink = VGroup(splitsqrt[0], splitsqrt[9], splitsqrt[21], splitsqrt[24])
		# Make elements grow briefly
		self.play(
			*[x.animate.scale(1.1).set_stroke(width=2) for x in blink],
			run_time=0.5
		)
		# Shrink and turn red
		self.play(
			*[x.animate.scale(0.90909).set_stroke(width=2).set_color(RED) for x in blink],
			run_time=0.5
		)
		self.wait(0.3)

		formula8[7].shift(RIGHT*1.05)
		
		# Shift destination elements over
		lpar_temp = splitsqrt[1].copy().set_opacity(0)
		rpar_temp = splitsqrt[8].copy().set_opacity(0)
		lroot_temp = splitsqrt[0].copy().set_opacity(0)
		lsqr_temp = splitsqrt[9].copy().set_opacity(0)
		
		roottemp = splitsqrt[21].copy().set_opacity(0)
		sqr_temp = splitsqrt[24].copy().set_opacity(0)

		lpar_temp.shift(LEFT*0.4)
		rpar_temp.shift(LEFT*0.55)
		lroot_temp.shift(LEFT*0.4)
		lsqr_temp.shift(LEFT*0.6)
		roottemp.shift(LEFT*1.2)
		sqr_temp.shift(LEFT*1.2)
		
		
		self.play(*[
			ReplacementTransform(splitsqrt[x], formula8[y])
			for x, y in zip(changes[11][0], changes[11][1])],
			# Write plus or minus
			Write(formula8[7]),
			formula8[7].animate.shift(LEFT),
			
			# Fade out sqrts and squares
			ReplacementTransform(splitsqrt[21], roottemp),
			ReplacementTransform(splitsqrt[24], sqr_temp),
			
			ReplacementTransform(splitsqrt[1], lpar_temp),
			ReplacementTransform(splitsqrt[8], rpar_temp),
			ReplacementTransform(splitsqrt[0], lroot_temp),
			ReplacementTransform(splitsqrt[9], lsqr_temp),

			run_time=2
		)
		# Add final formula 8 and remove temporary elements
		self.add(formula8)
		self.remove(lsqr_temp, lroot_temp, rpar_temp, lpar_temp, roottemp, sqr_temp)
		
		self.wait(1)

		# group b/2a elements in formula 8 and in formula 9
		f8group = VGroup(formula8[1:6])
		f9group = VGroup(formula9[13:18])
		self.play(*[
			ReplacementTransform(formula8[x], formula9[y])
			for x, y in zip(changes[12][0], changes[12][1])],
			# Swing b/2a over from left to right side
			CounterclockwiseTransform(f8group, f9group, path_arc=PI*0.8),
			run_time=1.75
		)

		self.wait(1)
		self.remove(f8group)

		# Final transformation: simplify right side
		self.play(*[
			ReplacementTransform(formula9[x], formula10[y])
			for x, y in zip(changes[13][0], changes[13][1])],
			formula9[13].animate.shift(UP*0.8),
			CounterclockwiseTransform(formula9[13], formula10[2], path_arc=PI*0.8),
			CounterclockwiseTransform(formula9[14], formula10[3], path_arc=PI*0.6),
			run_time=1.5
		)
		self.add(formula10)
		self.remove(formula9[13], formula9[14])
		self.wait(3)
		# Transforms everything back to original formula for GIF looping
		# self.play(
		# 	ReplacementTransform(formula10, formula))
		# self.wait(1)
		# self.play(
		# 	Unwrite(formula),
		# 	run_time=1)
