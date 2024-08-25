from manim import *

class RecurrenceRelationNew(Scene):
    def construct(self):
        # Create the text objects for the new lines
        generalizing_text = Text("On generalising,")
        recurrence_relation_text = MathTex(r"T(n) = n \cdot (n-1) \cdot (n-2) \cdot (n-3) \cdot (n-4) \cdot \ldots \cdot T(1)")
        simplified_relation_text = MathTex(r"T(n) = n \cdot (n-1) \cdot (n-2) \cdot (n-3) \cdot (n-4) \cdot \ldots \cdot 1")
        leading_term_text = Tex(r"Leading term is $n!$.")
        complexity_text = Tex(r"So, time complexity is $O(n!)$.")

        # Position the text objects
        generalizing_text.to_edge(UP)
        recurrence_relation_text.next_to(generalizing_text, DOWN, buff=0.5)
        simplified_relation_text.next_to(recurrence_relation_text, DOWN, buff=0.5)
        leading_term_text.next_to(simplified_relation_text, DOWN, buff=0.5)
        complexity_text.next_to(leading_term_text, DOWN, buff=0.5)

        # Display each text object sequentially with animations
        self.play(Write(generalizing_text))
        self.wait(1)
        self.play(Write(recurrence_relation_text))
        self.wait(1)
        self.play(Write(simplified_relation_text))
        self.wait(1)
        self.play(Write(leading_term_text))
        self.wait(1)
        self.play(Write(complexity_text))
        self.wait(2)

# Run the scene
if __name__ == "__main__":
    from manim import config, tempconfig
    config.media_dir = "media"
    config.quality = "low_quality"
    config.write_to_movie = True
    config.movie_file_extension = ".mp4"
    config.pixel_height = 720
    config.pixel_width = 1280
    tempconfig.update(
        {"background_color": BLACK}
    )
    scene = RecurrenceRelationNew()
    scene.render()
