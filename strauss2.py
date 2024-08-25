from manim import *

class RecurrenceRelation(Scene):
    def construct(self):
        # Title
        title = Text("On Tracking Back:\n", font_size=24, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Define the text lines with superscripts
        lines = [
            (r"T\left(\frac{n}{8}\right) = 7T\left(\frac{n}{16}\right) + \left(\frac{n}{8}\right)^{2}", 
             r"T\left(\frac{n}{8}\right) = 49T\left(\frac{n}{32}\right) + 7\left(\frac{n}{16}\right)^{2} + \left(\frac{n}{8}\right)^{2}", 
             r"T\left(\frac{n}{8}\right) = 49T\left(\frac{n}{32}\right) + \frac{11n^{2}}{256}"),
            (r"T\left(\frac{n}{4}\right) = 7T\left(\frac{n}{8}\right) + \left(\frac{n}{4}\right)^{2}", 
             r"T\left(\frac{n}{4}\right) = 343T\left(\frac{n}{32}\right) + \frac{77n^{2}}{256} + \left(\frac{n}{4}\right)^{2}", 
             r"T\left(\frac{n}{4}\right) = 343T\left(\frac{n}{32}\right) + \frac{93n^{2}}{256}"),
            (r"T\left(\frac{n}{2}\right) = 7T\left(\frac{n}{4}\right) + \left(\frac{n}{2}\right)^{2}", 
             r"T\left(\frac{n}{2}\right) = 2401T\left(\frac{n}{32}\right) + \frac{651n^{2}}{256} + \left(\frac{n}{2}\right)^{2}", 
             r"T\left(\frac{n}{2}\right) = 2401T\left(\frac{n}{32}\right) + \frac{715n^{2}}{256}"),
            (r"T(n) = 7T\left(\frac{n}{2}\right) + n^{2}", 
             r"T(n) = 16807T\left(\frac{n}{32}\right) + \frac{5005n^{2}}{256} + n^{2}", 
             r"T(n) = 16807T\left(\frac{n}{32}\right) + \frac{5261n^{2}}{256}")
        ]

        # Define the initial position of the first line
        initial_position = title.get_bottom() + DOWN * 1.2  # Positioned just below the title text
        
        # Iterate over the lines
        for i, (initial, intermediate, final) in enumerate(lines):
            # Position for the current line
            position = initial_position + DOWN * i * 1  # spacing out the lines
            
            # Create text objects with bold formatting
            initial_text = MathTex(initial, font_size=24).move_to(position)
            intermediate_text = MathTex(intermediate, font_size=24).move_to(position)
            final_text = MathTex(final, font_size=24).move_to(position)

            # Apply bold formatting using LaTeX commands
            initial_text = MathTex(r"\mathbf{" + initial + r"}", font_size=24).move_to(position)
            intermediate_text = MathTex(r"\mathbf{" + intermediate + r"}", font_size=24).move_to(position)
            final_text = MathTex(r"\mathbf{" + final + r"}", font_size=24).move_to(position)

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
