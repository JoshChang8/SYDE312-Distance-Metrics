from manim import *
import numpy as np

class DistanceMetricsIntro(Scene):
    def construct(self):
        # Main title (2 seconds)
        title = Text("Distance Metrics in Machine Learning", font_size=48).to_edge(UP)
        self.play(Write(title), run_time=2)
        
        # Wait for 2 seconds after displaying the title
        self.wait(2)
        
        # Create metrics sequentially for a total of approximately 10 seconds
        self.show_sequential_metrics()
        
        # Fade out title (0.5 seconds)
        self.play(FadeOut(title), run_time=0.5)

        
    def show_sequential_metrics(self):
        # Define points to use in all visualizations
        point_a = [1, 1]
        point_b = [4, 3]
        vector_a = [3, 1]
        vector_b = [2, 4]
        
        # Position for all sections
        pos_left = LEFT * 4
        pos_center = ORIGIN
        pos_right = RIGHT * 4
        
        # =============== EUCLIDEAN DISTANCE (First) ===============
        # Create and position Euclidean section
        euclidean_axes, euclidean_title = self.create_base_section("Euclidean Distance", BLUE, False)
        euclidean_axes.move_to(pos_left)
        euclidean_title.next_to(euclidean_axes, DOWN, buff=0.3)
        
        # Show Euclidean axes and title (0.5 seconds)
        self.play(
            Create(euclidean_axes),
            Write(euclidean_title),
            run_time=0.5
        )
        
        # Add Euclidean points (0.5 seconds)
        dot_a_euc = Dot(euclidean_axes.coords_to_point(*point_a), color=RED)
        dot_b_euc = Dot(euclidean_axes.coords_to_point(*point_b), color=GREEN)
        
        self.play(
            FadeIn(dot_a_euc),
            FadeIn(dot_b_euc),
            run_time=0.5
        )
        
        # Add point labels
        label_a_euc = Text("A", font_size=20, color=RED).next_to(dot_a_euc, DOWN, buff=0.1)
        label_b_euc = Text("B", font_size=20, color=GREEN).next_to(dot_b_euc, DOWN, buff=0.1)
        self.play(Write(label_a_euc), Write(label_b_euc), run_time=0.3)
        
        # Draw Euclidean line (0.7 seconds)
        euclidean_line = Line(dot_a_euc.get_center(), dot_b_euc.get_center(), color=YELLOW)
        self.play(Create(euclidean_line), run_time=0.7)
        
        # Wait a moment on completed Euclidean visualization
        self.wait(0.3)
        
        # =============== MANHATTAN DISTANCE (Second) ===============
        # Create and position Manhattan section
        manhattan_axes, manhattan_title = self.create_base_section("Manhattan Distance", RED, False)
        manhattan_axes.move_to(pos_center)
        manhattan_title.next_to(manhattan_axes, DOWN, buff=0.3)
        
        # Show Manhattan axes and title (0.5 seconds)
        self.play(
            Create(manhattan_axes),
            Write(manhattan_title),
            run_time=0.5
        )
        
        # Add Manhattan points (0.3 seconds)
        dot_a_man = Dot(manhattan_axes.coords_to_point(*point_a), color=RED)
        dot_b_man = Dot(manhattan_axes.coords_to_point(*point_b), color=GREEN)
        
        self.play(
            FadeIn(dot_a_man),
            FadeIn(dot_b_man),
            run_time=0.3
        )
        
        # Add point labels
        label_a_man = Text("A", font_size=20, color=RED).next_to(dot_a_man, DOWN, buff=0.1)
        label_b_man = Text("B", font_size=20, color=GREEN).next_to(dot_b_man, UP, buff=0.1)  # Changed to UP
        self.play(Write(label_a_man), Write(label_b_man), run_time=0.3)
        
        # Draw Manhattan path - horizontal then vertical (1.0 second)
        h_line = Line(
            manhattan_axes.coords_to_point(*point_a),
            manhattan_axes.coords_to_point(point_b[0], point_a[1]),
            color=ORANGE
        )
        v_line = Line(
            manhattan_axes.coords_to_point(point_b[0], point_a[1]),
            manhattan_axes.coords_to_point(*point_b),
            color=ORANGE
        )
        
        self.play(Create(h_line), run_time=0.5)
        self.play(Create(v_line), run_time=0.5)
        
        # Wait a moment on completed Manhattan visualization
        self.wait(0.3)
        
        # =============== COSINE SIMILARITY (Third) ===============
        # Create and position Cosine section
        cosine_axes, cosine_title = self.create_base_section("Cosine Similarity", GREEN, True)
        cosine_axes.move_to(pos_right)
        cosine_title.next_to(cosine_axes, DOWN, buff=0.3)
        
        # Show Cosine axes and title (0.5 seconds)
        self.play(
            Create(cosine_axes),
            Write(cosine_title),
            run_time=0.5
        )
        
        # Get origin point for vectors
        origin = cosine_axes.coords_to_point(0, 0)
        
        # Create and animate vector arrows (0.8 seconds) - ensuring they start at origin
        arrow_a = Arrow(origin, cosine_axes.coords_to_point(*vector_a), color=RED, max_tip_length_to_length_ratio=0.2, buff=0)
        arrow_b = Arrow(origin, cosine_axes.coords_to_point(*vector_b), color=GREEN, max_tip_length_to_length_ratio=0.2, buff=0)
        
        self.play(GrowArrow(arrow_a), GrowArrow(arrow_b), run_time=0.8)
        
        # Add vector labels
        label_a_cos = Text("A", font_size=20, color=RED).next_to(arrow_a.get_end(), RIGHT, buff=0.1)
        label_b_cos = Text("B", font_size=20, color=GREEN).next_to(arrow_b.get_end(), UP, buff=0.1)
        self.play(Write(label_a_cos), Write(label_b_cos), run_time=0.3)
        
        # Draw angle arc and theta label (0.8 seconds)
        angle = Angle(arrow_a, arrow_b, radius=0.5, color=YELLOW)
        
        # Position theta label at the middle of the angle
        angle_center = angle.get_center() + np.array([0.1, 0.1, 0])
        theta_label = MathTex("\\theta", font_size=24, color=YELLOW).move_to(angle_center)
        
        self.play(Create(angle), run_time=0.5)
        self.play(Write(theta_label), run_time=0.3)
        
        # Final pause (0.5 seconds)
        self.wait(0.5)
        
        # Fade out everything
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.3)
    
    def create_base_section(self, title_text, title_color, is_vector=False):
        # Create coordinate system based on whether it's for vectors or points
        if is_vector:
            axes = Axes(
                x_range=[-1, 5],
                y_range=[-1, 5],
                x_length=3.5,
                y_length=3.5,
                axis_config={"include_tip": True, "include_numbers": False}
            )
        else:
            axes = Axes(
                x_range=[0, 5],
                y_range=[0, 5],
                x_length=3.5,
                y_length=3.5,
                axis_config={"include_tip": True, "include_numbers": False}
            )
        
        # Title below
        title = Text(title_text, font_size=24, color=title_color)
        
        return axes, title
    
# To render using Manim CLI:
# manim -p -ql intro_conclusion.py DistanceMetricsIntro
# manim -p -ql intro_conclusion.py ConclusionScene