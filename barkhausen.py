from manim import *

class barkhausen(Scene):
    def construct(self):
        # Create circuit elements
        rect_loop = Rectangle(height=1.9, width=4)
        rect_loop.shift(1.12 * DOWN)
        rect_loop.shift(0.3 * RIGHT)
        amplifier = Triangle(fill_color=BLUE, fill_opacity=0.8)
        amplifier.rotate(30*DEGREES)
        feedback = Rectangle(height=1, width=2, fill_color=YELLOW, fill_opacity=0.8)
        
        # Position circuit elements
        feedback.next_to(amplifier, DOWN, buff=1)
        
        # Add labels
        amplifier_label = MathTex("\\text{Amplifier}").next_to(amplifier, UP, buff=0.5)
        feedback_label = MathTex("\\text{Feedback (LC Tank)}").next_to(feedback, DOWN, buff=0.5)
        
        # Create circuit connections
        circuit = VGroup(amplifier, feedback, amplifier_label, feedback_label).scale(0.8)
        
        # Animate circuit creation
        # Add text for Barkhausen criteria
        text = MathTex(r"\text{Barkhausen Criteria:}").to_edge(UP)
        text_1 = MathTex(r"\text{1. Gain $\geq$ 1}").next_to(text, DOWN).align_to(text, LEFT)
        text_2 = MathTex(r"\text{2. Phase Shift = $2\pi k$}").next_to(text_1, DOWN).align_to(text_1, LEFT)

        self.play(Write(text))
        self.wait(2)
        self.play(Write(text_1))
        self.wait(1)
        self.play(Write(text_2))
        self.wait(2)

        self.play(Create(rect_loop), Create(circuit))
        self.wait(3)
