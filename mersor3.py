from manim import *

class RecurrenceRelation(Scene):
    def construct(self):
        # Create the text objects
        generalizing_text = Text("On generalizing,")
        recurrence_relation_text = MathTex(r"T(n) = 2^k T\left(\frac{n}{2^k}\right) + kn")
        base_case_text = Tex(r"To reach base case, $n = 2^k$. So, $k = \log n$")
        log_base_case_text = MathTex(r"T(n) = 2^{\log n} \cdot T(1) + n \log n")
        simplify_text = MathTex(r"T(n) = n + n \log n")
        complexity_text = Tex(r"Leading term is $n \log n$. So, time complexity is $O(n \log n)$.")

        # Position the text objects
        generalizing_text.to_edge(UP)
        recurrence_relation_text.next_to(generalizing_text, DOWN, buff=0.5)
        base_case_text.next_to(recurrence_relation_text, DOWN, buff=0.5)
        log_base_case_text.next_to(base_case_text, DOWN, buff=0.5)
        simplify_text.next_to(log_base_case_text, DOWN, buff=0.5)
        complexity_text.next_to(simplify_text, DOWN, buff=0.5)

        # Display each text object sequentially with animations
        self.play(Write(generalizing_text))
        self.wait(1)
        self.play(Write(recurrence_relation_text))
        self.wait(1)
        self.play(Write(base_case_text))
        self.wait(1)
        self.play(Write(log_base_case_text))
        self.wait(1)
        self.play(Write(simplify_text))
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
    scene = RecurrenceRelation()
    scene.render()
