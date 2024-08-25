from manim import *

class RecurrenceRelation(Scene):
    def construct(self):
        # Title
        title = Text("Visualization of the Recurrence Relation\n\n", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Base case text
        base = Text("On tracking back:\n", font_size=24)
        base.to_edge(UP)
        base.next_to(title, DOWN)
        self.play(Write(base))
        self.wait(1)
        
        # Define the text lines
        lines = [
            ("T(n-3) = 3T(n-4)", "T(n-3) = 9T(n-5)"),
            ("T(n-2) = 3T(n-3)", "T(n-2) = 27T(n-5)"),
            ("T(n-1) = 3T(n-2)", "T(n-1) = 81T(n-5)"),
            ("T(n) = 3T(n-1)", "T(n) = 243T(n-5)")
        ]

        # Define the initial position of the first line
        initial_position = base.get_bottom() + DOWN * 1.2  # Positioned just below the base case text
        
        # Iterate over the lines
        for i, (initial, final) in enumerate(lines):
            # Position for the current line
            position = initial_position + DOWN * i * 1  # spacing out the lines
            
            # Create text objects
            initial_text = Text(initial, font_size=24).move_to(position)
            final_text = Text(final, font_size=24).move_to(position)

            # Display the initial text
            self.play(Write(initial_text))
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
