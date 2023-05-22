from manim import *

class natfreq(Scene):
    def construct(self):
        # eqs
        kvl = MathTex('L', '\\frac{dI}{dt} +', '{Q', '\\over', 'C}', ' = 0').scale(0.6)
        eq2 = MathTex('L', '\\frac{dI}{dt} = -', '{Q', '\\over', 'C}').scale(0.6)
        eq3 = MathTex('L', '\\frac{d^2Q}{dt} = -', '{Q', '\\over', 'C}').scale(0.6)
        eq4 = MathTex('L', '\\ddot{', 'Q', '}= -', '{Q', '\\over', 'C}').scale(0.6)
        eq5 = MathTex('\\ddot{', 'Q}', '= -', '{Q', '\\over', 'L', 'C}').scale(0.6)
        eq6 = MathTex('Q', '= Q_0 \\sin(', '{1 \\over', '\\sqrt{', 'L', 'C}}', 't + \\phi', ')').scale(0.6)
        eq7 = MathTex('\\omega = ', '{1 \\over', '\\sqrt{', 'L', 'C}}').scale(0.6)

        # Positioning
        kvl.to_edge(UP)
        eq2.next_to(kvl, DOWN, buff=0.25)
        eq3.next_to(eq2, DOWN, buff=0.25)
        eq4.next_to(eq3, DOWN, buff=0.25)
        eq5.next_to(eq4, DOWN, buff=0.25)
        eq6.next_to(eq5, DOWN, buff=0.25)
        eq7.next_to(eq6, DOWN, buff=0.25)

        # Animation
        prev = kvl
        eq_list = [kvl, eq2, eq3, eq4, eq5, eq6, eq7]
        color_map = {
                'Q': GREEN,
                'C': YELLOW,
                'L': BLUE
        }

        eq_cache = []
        for eq in eq_list:
            eq.set_color_by_tex_to_color_map(color_map)
            copy = prev.copy()
            eq_cache.append(copy)
            new_eq = Transform(copy, eq)
            self.play(new_eq)
            self.wait()
            prev = eq

        self.wait()

        self.play(*([FadeOut(eq) for eq in eq_cache]))

        eq8 = MathTex('\\omega_{\\text{natural}} = ', '{1 \\over', '\\sqrt{', 'L', 'C}}').scale(0.6)
        eq8.set_color_by_tex_to_color_map(color_map)
        eq8.move_to(ORIGIN)
        self.play(Write(eq8))
        self.wait()

        eq9 = MathTex('\\omega_{\\text{natural}} = \\omega_{\\text{resonant}} = ', '{1 \\over', '\\sqrt{', 'L', 'C}}').scale(0.6)
        eq9.set_color_by_tex_to_color_map(color_map)
        eq9.move_to(ORIGIN)
        self.play(Transform(eq8, eq9))
        self.wait()

