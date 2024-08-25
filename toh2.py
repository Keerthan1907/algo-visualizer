from manim import *

class RecurrenceRelation(Scene):
    def construct(self):
        # Title
        
        
        # Base case text
        base = Text("On tracking back:\n", font_size=24)
        base.to_edge(UP)
        self.play(Write(base))
        self.wait(1)
        
        # Define the text lines
        lines = [
            ("T(n-3) = 2T(n-4) + c", "T(n-3) = 4T(n-5) + c + c", "T(n-3) = 4T(n-5) + 2c"),
            ("T(n-2) = 2T(n-3) + c", "T(n-2) = 8T(n-5) + 4c + c", "T(n-2) = 8T(n-5) + 5c"),
            ("T(n-1) = 2T(n-2) + c", "T(n-1) = 16T(n-5) + 10c + c", "T(n-1) = 16T(n-5) + 11c"),
            ("T(n) = 2T(n-1) + c", "T(n) = 32T(n-5) + 22c + c", "T(n) = 32T(n-5) + 23c")
        ]

        # Define the initial position of the first line
        initial_position = base.get_bottom() + DOWN * 1.2  # Positioned just below the base case text
        
        # Iterate over the lines
        for i, (initial, intermediate, final) in enumerate(lines):
            # Position for the current line
            position = initial_position + DOWN * i * 1  # spacing out the lines
            
            # Create text objects
            initial_text = Text(initial, font_size=24).move_to(position)
            intermediate_text = Text(intermediate, font_size=24).move_to(position)
            final_text = Text(final, font_size=24).move_to(position)

            # Display the initial text
            self.play(Write(initial_text))
            self.wait(1)

            # Transform to intermediate text
            self.play(Transform(initial_text, intermediate_text))
            self.wait(1)

            # Transform to final text
            self.play(Transform(initial_text, final_text))
            self.wait(1)

        # Instructions to run the code:
        # 1. Ensure you have Manim Community installed. If not, you can install it using pip:
        #    pip install manim
        # 2. Save the code in a Python file, for example, recurrence_relation.py.
        # 3. Run the Manim command to render the animation:
        #    manim -pql recurrence_relation.py RecurrenceRelation

