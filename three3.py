from manim import *

class DisplayRecurrenceRelation(Scene):
    def construct(self):
        # List of lines to be displayed
        lines = [
            "On generalising,",
            "T(n) = (3^k)T(n-k)",
            "To reach the base case, assume n-k=0, k=n",
            "T(n) = (3^n)T(0) = 3^n",
            "So, Time Complexity: O(3^n)"
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
