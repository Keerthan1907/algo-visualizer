from manim import *

class DisplayRecurrenceRelation(Scene):
    def construct(self):
        # List of lines to be displayed
        lines = [
            "On Generalizing: T(n) = 7^k T(n / 2^k) + n^2 * sum of coefficients",
            "To reach the base case: 2^k = n and k = log (n)",
            "Substitute k = log2(n):",
            "T(n) = 7^log(n) * T(1) + n^2 * sum of coefficients",
            "T(n) = n^log(7) * T(1) + n^2",
            "T(n) = n^log(7) * 1 + n^2",
            "T(n) = n^log(7) + n^2",
            "The leading term is  n^log(7) = n^2.81. So, the time complexity is O(n^2.81)."
        ]
        
        # Create text objects for each line
        text_objects = [Text(line) for line in lines]
        
        # Display each text object one after the other
        for text in text_objects:
            self.play(Write(text))
            self.wait(2)  # Adjust the wait time if needed
            self.play(FadeOut(text))

if __name__ == "__main__":
    from manim import cli
    cli.main()
