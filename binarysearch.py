from manim import *

class RecurrenceRelation(Scene):
    def construct(self):
        # Title
        title = Text("Visualization of the Binary Search Animation\n\n", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)



        base = Text("The base case for this equation is : T(1) = 1\n\n", font_size=24)
        base.next_to(title, DOWN)
        self.play(Write(base))
        self.wait(1)



        # Define the text lines
        lines = [
            "T(n) = T(n/2) + c",
            "T(n/2) = T(n/4) + c",
            "T(n/4) = T(n/8) + c",
            "T(n/8) = T(n/16) + c",
            "T(n/16) = T(n/32) + c"
            # "Tracking back",
            # "t(n/4) = t(n/16) + 2c",
            # "t(n/2) = t(n/16) + 3c",
            # "t(n) = t(n/16) + 4c",
            # "On generalising, t(n) = t(n/2^k) + kc",
            # "To reach base case, 2^k should become equal to n",
            # "So if 2^k = n, k = log n",
            # "So t(n) = t(n/n) + log n * c",
            # "t(n) = t(1) + log n * c",
            # "t(1) = 1",
            # "t(n) = 1 + log n * c",
            # "1 and c are constants.",
            # "So time complexity is O(log n)."
        ]

        # Define the initial position of the first line
        initial_position = UP * 2
        
        # Create text objects for each line
        text_objects = [Text(line, font_size=24) for line in lines]

        # Display the first line
        self.play(Write(text_objects[0].move_to(initial_position)))
        self.wait(1)

        # Manually handle the movement of t(n/2), t(n/4), etc.
        for i in range(1, 5):
            # Calculate the position for the next line
            new_position = initial_position + DOWN * i

            # Extract the part to move
            rhs_part_to_move = lines[i - 1].split('=')[1].strip().split('+')[0].strip()  # right-hand side part to move

            part_to_move = Text(rhs_part_to_move, font_size=24).move_to(new_position + LEFT * 3)
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

        # Display the remaining lines without movement
        # for i in range(5, len(lines)):
        #     new_position = initial_position + DOWN * i
        #     self.play(Write(text_objects[i].move_to(new_position)))
        #     self.wait(1)

# Instructions to run the code:
# 1. Ensure you have Manim Community installed. If not, you can install it using pip:
#    pip install manim
# 2. Save the code in a Python file, for example, recurrence_relation.py.
# 3. Run the Manim command to render the animation:
#    manim -pql recurrence_relation.py RecurrenceRelation
