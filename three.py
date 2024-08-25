from manim import *

class RecurrenceRelationExample(Scene):
    def construct(self):
        # Title
        title = Text("Visualization of the Reccurence Relation\n\n", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Base case
        base = Text("The base case for this equation is : T(0) = 1\n\n", font_size=24)
        base.next_to(title, DOWN)
        self.play(Write(base))
        self.wait(1)

        # Define the text lines
        lines = [
            "T(n) = 3T(n-1)",
            "T(n-1) = 3T(n-2)",
            "T(n-2) = 3T(n-3)",
            "T(n-3) = 3T(n-4)",
            "T(n-4) = 3T(n-5)"
        ]

        # Define the initial position of the first line
        initial_position = UP * 2
        
        # Create text objects for each line
        text_objects = [Text(line, font_size=24) for line in lines]

        # Display the first line
        self.play(Write(text_objects[0].move_to(initial_position)))
        self.wait(1)

        # Manually handle the movement of T(n-1), T(n-2), etc.
        for i in range(1, 5):
            # Calculate the position for the next line
            new_position = initial_position + DOWN * i

            # Extract the part to move
            rhs_part_to_move = lines[i - 1].split('=')[1].strip()  # right-hand side part to move

            part_to_move = (Text(rhs_part_to_move, font_size=24).move_to(new_position + LEFT * 3))[1:]
            # Create the rest of the line without the part to move
            rest_of_line = Text(f"= {lines[i][8:]}", font_size=24).next_to(part_to_move, RIGHT)

            # Animate the part moving and then display the rest of the line
            self.play(Transform(text_objects[i - 1].copy(), part_to_move))
            self.wait(1)
            self.play(Write(rest_of_line))

            # Combine the moved part and the rest of the line
            combined_text = VGroup(part_to_move, rest_of_line)
            text_objects[i] = combined_text
            self.add(combined_text)
            self.wait(1)

# Instructions to run the code:
# 1. Ensure you have Manim Community installed. If not, you can install it using pip:
#    pip install manim
# 2. Save the code in a Python file, for example, recurrence_relation_example.py.
# 3. Run the Manim command to render the animation:
#    manim -pql recurrence_relation_example.py RecurrenceRelationExample
