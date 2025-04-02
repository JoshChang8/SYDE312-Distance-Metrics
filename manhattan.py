from manim import *

class CombinedManhattanScene(Scene):
    def construct(self):
        # === Scene 0 ===
        title = Text("Manhattan Distance", font_size=72)
        self.play(FadeIn(title, shift=UP), run_time=2)
        self.wait(13)  # Hold on screen for 15s total with 2s fade-in
        self.clear()

        # === Scene 1 ===
        title = Text("How it Works", font_size=32).to_edge(UP)
        self.play(Write(title))
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], axis_config={"include_numbers": True})
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        self.play(Create(axes), Write(x_label), Write(y_label))

        point_a_coords = (1, 1)
        point_b_coords = (3, 4)
        point_a = axes.c2p(*point_a_coords)
        point_b = axes.c2p(*point_b_coords)
        dot_a = Dot(point_a, color=BLUE)
        dot_b = Dot(point_b, color=RED)
        label_a = MathTex("A(1,1)").next_to(dot_a, DOWN)
        label_b = MathTex("B(3,4)").next_to(dot_b, UP)
        self.play(FadeIn(dot_a), Write(label_a))
        self.play(FadeIn(dot_b), Write(label_b))

        buildings = VGroup()
        for x, y in [(2, 2), (2.5, 3), (2.5, 2)]:
            b = Rectangle(width=0.8, height=0.8, color=GREY, fill_opacity=0.6).move_to(axes.c2p(x, y))
            buildings.add(b)
        self.play(FadeIn(buildings))
        self.wait(8)

        diag_line = DashedLine(start=point_a, end=point_b, color=YELLOW)
        self.play(Create(diag_line))
        self.wait(5)

        mid_point = axes.c2p(3, 1)
        horiz_line = Line(point_a, mid_point, color=GREEN)
        vert_line = Line(mid_point, point_b, color=GREEN)
        self.play(Create(horiz_line))
        self.play(Create(vert_line))
        self.wait(10)

        self.clear()
        self.wait(3)

        # === Scene 2 ===
        # Create title and formula centered and spaced
        title = Text("Mathematical Formula", font_size=32)
        formula = MathTex(r"\text{Manhattan Distance} = |x_1 - x_2| + |y_1 - y_2|")

        title_group = VGroup(title, formula).arrange(DOWN, center=True, buff=0.3)
        title_group.to_edge(UP)

        self.play(Write(title))
        self.play(Write(formula))
        self.wait(0.5)

        axes = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], axis_config={"include_numbers": True}).scale(0.75).to_edge(LEFT)
        point_a = axes.c2p(1, 1)
        point_b = axes.c2p(3, 4)
        dot_a = Dot(point_a, color=BLUE)
        dot_b = Dot(point_b, color=RED)
        label_a = MathTex("A(1,1)").scale(0.6).next_to(dot_a, DOWN)
        label_b = MathTex("B(3,4)").scale(0.6).next_to(dot_b, UP)
        buildings = VGroup(*[Rectangle(width=0.8, height=0.8, color=GREY, fill_opacity=0.6).move_to(axes.c2p(x, y)) for x, y in [(2, 2), (2.5, 3), (2.5, 2)]])
        diag_line = DashedLine(point_a, point_b, color=YELLOW)
        horiz = Line(point_a, axes.c2p(3, 1), color=GREEN)
        vert = Line(axes.c2p(3, 1), point_b, color=GREEN)

        self.play(Create(axes), FadeIn(dot_a), Write(label_a), FadeIn(dot_b), Write(label_b))
        self.play(FadeIn(buildings), Create(diag_line))
        self.wait(1)
        self.play(Create(horiz), Create(vert))

        calc_steps = VGroup(
            MathTex(r"A(1,1),\quad B(3,4)"),
            MathTex(r"= |1 - 3| + |1 - 4|"),
            MathTex(r"= 2 + 3"),
            MathTex(r"= 5")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.9).to_edge(RIGHT)
        for step in calc_steps:
            self.play(Write(step))
            self.wait(0.5)
        self.wait(6)

        self.clear()
        self.wait(6) #adjust this 

        # === Scene 3 ===
        title = Text("Application 1: Pathfinding", font_size=32).to_edge(UP)
        self.play(Write(title))
        grid = NumberPlane(x_range=[0, 6, 1], y_range=[0, 6, 1], background_line_style={"stroke_opacity": 0.4}).scale(0.8)
        self.play(Create(grid))

        start_coords = (0, 0)
        delivery_coords = (2, 2)
        final_dropoff_coords = (5, 4)
        start = grid.c2p(*start_coords)
        delivery = grid.c2p(*delivery_coords)
        final_dropoff = grid.c2p(*final_dropoff_coords)

        buildings = VGroup()
        for x, y in [(3, 3), (3, 2), (4, 2), (4, 3), (0, 0), (0, 1), (1, 0), (1, 1)]:
            b = Rectangle(width=0.8, height=0.8, fill_color=GREY, fill_opacity=0.6, color=GREY).move_to(grid.c2p(x + 0.5, y + 0.5))
            buildings.add(b)
        self.play(FadeIn(buildings))
        self.wait(5)

        dot_start = Dot(start, color=BLUE).scale(1.2)
        dot_delivery = Dot(delivery, color=ORANGE).scale(1.2)
        dot_final = Dot(final_dropoff, color=RED).scale(1.2)
        label_start = Text("Start", font_size=24).next_to(dot_start, DOWN)
        label_delivery = Text("Delivery", font_size=24).next_to(dot_delivery, UP)
        label_final = Text("Dropoff", font_size=24).next_to(dot_final, UP)
        self.play(FadeIn(dot_start), FadeIn(dot_delivery), FadeIn(dot_final))
        self.play(Write(label_start), Write(label_delivery), Write(label_final))

        car = Dot(start, color=YELLOW).scale(1.5)
        self.add(car)
        self.wait(10) #change this for voice over

        p1 = Line(start, grid.c2p(2, 0), color=GREEN)
        p2 = Line(grid.c2p(2, 0), delivery, color=GREEN)
        self.play(Create(p1), car.animate.move_to(grid.c2p(2, 0)), run_time=2)
        self.play(Create(p2), car.animate.move_to(delivery), run_time=2)
        self.wait(5)

        p3 = Line(delivery, grid.c2p(2, 4), color=GREEN)
        p4 = Line(grid.c2p(2, 4), final_dropoff, color=GREEN)
        self.play(Create(p3), car.animate.move_to(grid.c2p(2, 4)), run_time=2)
        self.play(Create(p4), car.animate.move_to(final_dropoff), run_time=2)
        self.wait(5)

        self.clear()
        self.wait(3)

        # === Scene 4 ===
        title = Text("Application 2: Machine Learning", font_size=32).to_edge(UP)
        self.play(Write(title))
        axes = Axes(x_range=[0, 6, 1], y_range=[0, 6, 1], axis_config={"include_numbers": False}).scale(0.8)
        self.play(Create(axes), run_time=2)

        center_a = axes.c2p(1, 1)
        center_b = axes.c2p(5, 5)
        dot_a = Dot(center_a, color=BLUE).scale(1.2)
        dot_b = Dot(center_b, color=RED).scale(1.2)
        label_a = Text("Cluster A", font_size=24, color=BLUE).next_to(dot_a, DOWN)
        label_b = Text("Cluster B", font_size=24, color=RED).next_to(dot_b, UP)
        self.play(FadeIn(dot_a), FadeIn(dot_b), Write(label_a), Write(label_b), run_time=2)

        data_coords = [(2.5, 1.2), (3.2, 2.5), (4.5, 2.8), (2, 4), (4.1, 2.3)]
        data_points = [Dot(axes.c2p(x, y), color=WHITE).scale(0.8) for x, y in data_coords]
        self.play(*[FadeIn(p) for p in data_points], run_time=2)

        manhattan_lines = VGroup()
        assignments = []
        for x, y in data_coords:
            dist_a = abs(x - 1) + abs(y - 1)
            dist_b = abs(x - 5) + abs(y - 5)
            if dist_a < dist_b:
                h = Line(axes.c2p(x, y), axes.c2p(1, y), color=BLUE)
                v = Line(axes.c2p(1, y), center_a, color=BLUE)
                manhattan_lines.add(h, v)
                assignments.append('A')
            else:
                h = Line(axes.c2p(x, y), axes.c2p(5, y), color=RED)
                v = Line(axes.c2p(5, y), center_b, color=RED)
                manhattan_lines.add(h, v)
                assignments.append('B')
        self.play(*[Create(line) for line in manhattan_lines], run_time=3)
        self.wait(5)

        euclidean_lines = VGroup()
        for i, (point, assign) in enumerate(zip(data_points, assignments)):
            x, y = data_coords[i]
            if (x, y) == (2, 4):
                target_center = center_a
                color = BLUE
            else:
                target_center = center_a if assign == 'A' else center_b
                color = BLUE if assign == 'A' else RED
            line = DashedLine(point.get_center(), target_center, color=color, stroke_width=2)
            euclidean_lines.add(line)

        self.play(*[Create(line) for line in euclidean_lines], run_time=3)
        self.wait(4)

        solid_key = VGroup(Line(ORIGIN, RIGHT * 0.5, color=WHITE), Text("Manhattan Distance", font_size=20).next_to(RIGHT * 0.5, RIGHT, buff=0.2))
        dashed_key = VGroup(DashedLine(ORIGIN, RIGHT * 0.5, color=WHITE), Text("Euclidean Distance", font_size=20).next_to(RIGHT * 0.5, RIGHT, buff=0.2))
        legend = VGroup(solid_key, dashed_key).arrange(DOWN, aligned_edge=LEFT).to_corner(UR).shift(DOWN * 0.5 + LEFT * 0.5)
        self.play(FadeIn(legend), run_time=2)
        self.wait(3)