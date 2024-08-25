from manim import *

class RecurrenceRelation(Scene):
    def construct(self):
        # Define the LaTeX strings for the equations and derivations
        eq1 = MathTex(r"T(n-2) = 2T(n-4) + T(n-5)")
        eq2 = MathTex(r"T(n-1) = T(n-3) + 2T(n-4) + T(n-5)")
        eq3 = MathTex(r"T(n) = T(n-3) + 4T(n-4) + 2T(n-5)")
        eq4 = MathTex(r"T(n-3), T(n-4), T(n-5) \text{ can be further expanded.}")
        eq5 = MathTex(r"\text{So, the time complexity grows exponentially.}")
        eq6 = MathTex(r"\text{Time complexity is } O(2^n).")

        # Scale down the text
        equations = [eq1, eq2, eq3, eq4, eq5, eq6]
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
