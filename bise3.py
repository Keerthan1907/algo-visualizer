from manim import *

class RecurrenceRelation(Scene):
    def construct(self):
        # Create the text objects
        t_n_text = MathTex(r"T(n) = T\left(\frac{n}{2^k}\right) + kc")
        k_log_n_text = MathTex(r"2^k = n \implies k = \log n")
        t_n_evaluation_text = MathTex(r"T(n) = T\left(\frac{n}{n}\right) + \log n \cdot c")
        base_case_text = MathTex(r"T(n) = T(1) + \log n \cdot c")
        t_1_value_text = MathTex(r"T(1) = 1 \implies T(n) = 1 + \log n \cdot c")
        final_time_complexity_text = MathTex(r"T(n) = 1 + \log n \cdot c \text{ and thus, T(n) = } O(\log n)")

        # Position the text objects
        t_n_text.to_edge(UP)
        k_log_n_text.next_to(t_n_text, DOWN, buff=0.5)
        t_n_evaluation_text.next_to(k_log_n_text, DOWN, buff=0.5)
        base_case_text.next_to(t_n_evaluation_text, DOWN, buff=0.5)
        t_1_value_text.next_to(base_case_text, DOWN, buff=0.5)
        final_time_complexity_text.next_to(t_1_value_text, DOWN, buff=0.5)

        # Display each text object sequentially with animations
        self.play(Write(t_n_text))
        self.wait(1)
        self.play(Write(k_log_n_text))
        self.wait(1)
        self.play(Write(t_n_evaluation_text))
        self.wait(1)
        self.play(Write(base_case_text))
        self.wait(1)
        self.play(Write(t_1_value_text))
        self.wait(1)
        self.play(Write(final_time_complexity_text))
        self.wait(2)
