from manim import *

class npn(Scene):
    def construct(self):
        # Create components
        collector = Rectangle(height=1.5, width=2, fill_color=BLUE, fill_opacity=0.8)
        base = Rectangle(height=1, width=2, fill_color=RED, fill_opacity=0.8)
        emitter = Rectangle(height=1.5, width=2, fill_color=BLUE, fill_opacity=0.8)

        # Position components
        collector.next_to(base, UP, buff=0)
        emitter.next_to(base, DOWN, buff=0)

        # Add labels
        cn_label = Text('N').scale(0.3).move_to(collector.get_center())
        bp_label = Text('P').scale(0.3).move_to(base.get_center())
        en_label = Text('N').scale(0.3).move_to(emitter.get_center())
        collector_label = Text('Collector (N)').scale(0.3).move_to(collector.get_center())
        base_label = Text('Base (P)').scale(0.3).move_to(base.get_center())
        emitter_label = Text('Emitter (N)').scale(0.3).move_to(emitter.get_center())

        # Add connecting lines
        collector_c2e = Line(collector.get_edge_center(RIGHT), collector.get_edge_center(RIGHT) + RIGHT)
        emitter_c2e = Line(emitter.get_edge_center(RIGHT), emitter.get_edge_center(RIGHT) + RIGHT)
        base_b2e = Line(base.get_edge_center(LEFT), base.get_edge_center(LEFT) + LEFT)
        emitter_b2e = Line(emitter.get_edge_center(LEFT), emitter.get_edge_center(LEFT) + LEFT)
        c2e = Line(collector_c2e.get_right(), emitter_c2e.get_right())
        b2e = Line(base_b2e.get_left(), emitter_b2e.get_left())
        Vbe = MathTex('V_{BE}').scale(0.5).next_to(b2e.get_left(), LEFT)
        Vce = MathTex('V_{CE}').scale(0.5).next_to(c2e.get_right(), RIGHT)

        # Create transistor
        transistor = VGroup(collector, cn_label, base, bp_label, emitter, en_label)
        lines = VGroup(collector_c2e, emitter_c2e, base_b2e, emitter_b2e, c2e, b2e)

        # Animate the transistor
        self.play(Create(transistor))
        self.wait(3)
        self.play(Transform(cn_label, collector_label), Transform(bp_label, base_label), Transform(en_label, emitter_label), Create(lines))
        self.wait(2)
        self.play(Write(Vbe), Write(Vce))
        self.wait(2)
        Vbeg0 = MathTex('V_{BE} > 0').scale(0.5).set_color(GREEN).next_to(b2e.get_left(), LEFT)
        Vceg0 = MathTex('V_{CE} > 0').scale(0.5).set_color(GREEN).next_to(c2e.get_right(), RIGHT)
        current_arrow = Arrow(start=collector.get_center(), end=emitter.get_center(), color=GREEN)
        self.play(Transform(Vbe, Vbeg0))
        self.wait(0.5)
        self.play(Transform(Vce, Vceg0), Create(current_arrow))
        self.wait(2)

