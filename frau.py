from manim import *

class RecurrenceRelation(Scene):
    def construct(self):
        # Define the LaTeX strings for the equations and derivations
        eq1 = MathTex(r"T(n) = 7^k T\left(\frac{n}{2^k}\right) + n^2 \cdot \text{sum of coefficients}")
        eq2 = MathTex(r"\text{To reach the base case: } 2^k = n \text{ and } k = \log_2 (n)")
        eq3 = MathTex(r"\text{Substitute } k = \log_2(n):")
        eq4 = MathTex(r"T(n) = 7^{\log_2(n)} T(1) + n^2 \cdot \text{sum of coefficients}")
        eq5 = MathTex(r"T(n) = n^{\log_2(7)} \cdot T(1) + n^2")
        eq6 = MathTex(r"T(n) = n^{\log_2(7)} \cdot 1 + n^2")
        eq7 = MathTex(r"T(n) = n^{\log_2(7)} + n^2")
        eq8 = MathTex(r"\text{The leading term is } n^{\log_2(7)} = n^{2.81}")
        eq9 = MathTex(r"\text{So, the time complexity is } O(n^{2.81})")

        # Scale down the text
        equations = [eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9]
        for eq in equations:
            eq.scale(0.8)

        # Arrange the equations in a vertical column with reduced gap
        eq_group = VGroup(*equations).arrange(DOWN, buff=0.3)

        # Display the equations one by one
        for eq in eq_group:
            self.play(Write(eq))
            self.wait(2)
