from manim import *

class FibonacciRecurrenceRelation(Scene):
    def construct(self):
        # Title
        title = Text("Visualization of the Fibonacci Recurrence Relation\n\n", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Base case
        base = Text("The base cases for this equation are: T(0) = 0 and T(1) = 1\n\n", font_size=24)
        base.next_to(title, DOWN)
        self.play(Write(base))
        self.wait(1)

        # Define the text lines
        lines = [
            "T(n) = T(n-1) + T(n-2)",
            "T(n-1) = T(n-2) + T(n-3)",
            "T(n-2) = T(n-3) + T(n-4)",
            "T(n-3) = T(n-4) + T(n-5)",
            "T(n-4) = T(n-5) + T(n-6)"
        ]

        # Define the initial position of the first line
        initial_position = UP * 2

        # Create text objects for each line
        text_objects = [Text(line, font_size=24) for line in lines]

        # Display all lines sequentially
        for i, text_object in enumerate(text_objects):
            # Calculate the position for the next line
            new_position = initial_position + DOWN * i

            # Display the line
            self.play(Write(text_object.move_to(new_position)))
            self.wait(1)

# Instructions to run the code:
# 1. Ensure you have Manim Community installed. If not, you can install it using pip:
#    pip install manim
# 2. Save the code in a Python file, for example, fibonacci_recurrence_relation.py.
# 3. Run the Manim command to render the animation:
#    manim -pql fibonacci_recurrence_relation.py FibonacciRecurrenceRelation
