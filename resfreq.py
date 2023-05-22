from manim import *

class resfreq(Scene):
    def construct(self):
        # eqs
        imp = MathTex('Z', '=', '\\sqrt{', 'R^2', '+', '(', 'X_L', '-', 'X_C', ')^2').scale(0.6)
        eq2 = MathTex('Z', '=', '\\sqrt{', 'R^2', '+', '(', '2\\pi', 'f', 'L', '-', '{1 \\over', '2\\pi', 'f', 'C}', ')^2').scale(0.6)
        eq3 = MathTex('2\\pi', 'f', 'L', '=', '{1 \\over', '2\\pi', 'f', 'C}').scale(0.6)
        eq4 = MathTex('f', '^2', '=', '{1 \\over', '(2\\pi)^2', 'L', 'C}').scale(0.6)
        eq5 = MathTex('f', '=', '{1 \\over', '2\\pi', '\\sqrt{', 'L', 'C}}').scale(0.6)
        eq6 = MathTex('\\omega', '= 2\\pi', 'f').scale(0.6)
        eq7 = MathTex('\\omega', '= 2\\pi', '{1 \\over', '2\\pi', '\\sqrt{', 'L', 'C}}').scale(0.6)
        eq8 = MathTex('\\omega', '=', '{1 \\over', '\\sqrt{', 'L', 'C}}').scale(0.6)

        # Positioning
        imp.to_edge(UP)
        eq2.next_to(imp, DOWN, buff=0.25)
        eq3.next_to(eq2, DOWN, buff=0.25)
        eq4.next_to(eq3, DOWN, buff=0.25)
        eq5.next_to(eq4, DOWN, buff=0.25)
        eq6.next_to(eq5, DOWN, buff=0.25)
        eq7.next_to(eq6, DOWN, buff=0.25)
        eq8.next_to(eq7, DOWN, buff=0.25)

        # Animation
        prev = imp
        eq_list = [imp, eq2, eq3, eq4, eq5, eq6, eq7, eq8]
        color_map = {
                'Z': RED,
                'C': YELLOW,
                'L': BLUE,
                'f': GREEN
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
