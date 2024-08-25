from manim import *

class RecurrenceRelation(Scene):
    def construct(self):
        # Define the LaTeX strings for the equations and derivations
        eq1 = MathTex(r"\text{On generalising,}")
        eq2 = MathTex(r"T(n) = (2^k)T(n-k) + (2^k-1)c")
        eq3 = MathTex(r"\text{To reach base case, } k = n-1.")
        eq4 = MathTex(r"T(n) = \left(2^{n-1}\right)T(1) + \left(2^{n-1}-1\right)c")
        eq5 = MathTex(r"T(n) = \left(2^{n-1}\right) + \left(2^{n-1}-1\right)c")
        eq6 = MathTex(r"\text{The leading term is } 2^n.")
        eq7 = MathTex(r"\text{So, } O(n) = 2^n")

        # Scale down the text
        equations = [eq1, eq2, eq3, eq4, eq5, eq6, eq7]
        for eq in equations:
            eq.scale(0.8)

        # Arrange the equations in a vertical column with reduced gap
        eq_group = VGroup(*equations).arrange(DOWN, buff=0.3)

        # Display the equations one by one
        for eq in eq_group:
            self.play(Write(eq))
            self.wait(2)

# To run this code, save it to a file (e.g., recurrence_relation.py) and execute it using the Manim command:
# manim -pql recurrence_relation.py
