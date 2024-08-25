from manim import *

class RecurrenceRelation(Scene):
   
    def construct(self):
        # Base case text
        k=17
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
        
        # Define color ranges for the previous and current lines
        previous_color_range = (7, 17)  # Example range for previous lines
        current_color_range = (7, k)   # Example range for the current line
        k=k+2
        # Define color ranges for the last line
        last_line_previous_color_range = (7, 19)  # Example range for the previous part in the last line
        last_line_current_color_range = (5, 17)   # Example range for the current part in the last line
        
        # Iterate over the lines
        previous_final_text = None  # To store the final text of the previous iteration
        
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

            # Only color specific parts in the second line onwards
            if i > 0:
                # Determine the color ranges based on whether it's the last line
                if i == len(lines) - 1:
                    prev_color_range = last_line_previous_color_range
                    curr_color_range = last_line_current_color_range
                else:
                    prev_color_range = previous_color_range
                    curr_color_range = current_color_range

                # Color the specific part of the intermediate text
                colored_intermediate_text = Text(intermediate, font_size=24).move_to(position)
                colored_intermediate_text[curr_color_range[0]:curr_color_range[1]].set_color(RED)

                # Also color the corresponding part of the previous final text
                x=previous_final_text.copy()
                colored_previous_final_text = previous_final_text.copy()
                colored_previous_final_text[prev_color_range[0]:prev_color_range[1]].set_color(RED)

                # Transform the previous final text and current initial text simultaneously
                self.play(
                    Transform(previous_final_text, colored_previous_final_text),
                    Transform(initial_text, colored_intermediate_text)
                )
                self.wait(1)
                
                # Reset the colors to normal for the next step
                self.play(
                    Transform(previous_final_text, x.copy().move_to(previous_final_text.get_center())),
                    Transform(initial_text, final_text.copy().move_to(initial_text.get_center()))
                )
            else:
                # For the first line, just transform without color changes
                self.play(Transform(initial_text, intermediate_text))
                self.wait(1)    
                self.play(Transform(initial_text, final_text))
            
            self.wait(1)

            # Update previous_final_text for the next iteration
            previous_final_text = final_text

        # Instructions to run the code:
        # 1. Ensure you have Manim Community installed. If not, you can install it using pip:
        #    pip install manim
        # 2. Save the code in a Python file, for example, recurrence_relation.py.
        # 3. Run the Manim command to render the animation:
        #    manim -pql recurrence_relation.py RecurrenceRelation
