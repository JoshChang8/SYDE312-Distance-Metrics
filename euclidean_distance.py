from manim import *
import numpy as np
import random

class EuclideanDistanceVisualization(Scene):
    def construct(self):
        # Title that persists throughout the presentation
        title = Text("Understanding Euclidean Distance", font_size=40)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)  # Reduced wait time
        
        # SECTION 1: HISTORY - More Visual Approach with proper spacing
        section_title = Text("Brief History", font_size=36, color=BLUE)
        section_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(section_title))
        
        # Ancient Greece visual - left side with proper spacing
        greek_math = Text("Euclidean Geometry", font_size=30)
        greek_math.to_edge(LEFT, buff=2)
        greek_math.shift(DOWN)
        
        euclid_label = Text("Euclid (300 BCE)", font_size=24, color=BLUE)
        euclid_label.next_to(greek_math, UP, buff=0.3)
        
        pythagoras_theorem = MathTex("a^2 + b^2 = c^2", font_size=36)
        pythagoras_theorem.next_to(greek_math, DOWN, buff=0.5)
        
        # Modern math visual - right side with proper spacing
        modern_math = Text("Analytic Geometry", font_size=30)
        modern_math.to_edge(RIGHT, buff=2)
        modern_math.shift(DOWN)
        
        descartes_label = Text("Descartes (17th century)", font_size=24, color=GREEN)
        descartes_label.next_to(modern_math, UP, buff=0.3)
        
        # Properly sized formula with adequate spacing
        distance_formula = MathTex(r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}", font_size=32)
        distance_formula.next_to(modern_math, DOWN, buff=0.5)
        
        # Timeline arrow with proper positioning
        timeline = Arrow(
            greek_math.get_right() + RIGHT * 0.5, 
            modern_math.get_left() - RIGHT * 0.5, 
            buff=0.2,
            max_tip_length_to_length_ratio=0.05
        )
        timeline_text = Text("Evolution of Distance Concept", font_size=20)
        timeline_text.next_to(timeline, UP, buff=0.1)
        
        # Animate history section
        self.play(FadeIn(greek_math), Write(euclid_label))
        self.wait(0.5)  # Reduced wait time
        self.play(Write(pythagoras_theorem))
        self.wait(0.7)  # Reduced wait time
        
        self.play(Create(timeline), Write(timeline_text))
        self.wait(0.5)  # Reduced wait time
        
        self.play(FadeIn(modern_math), Write(descartes_label))
        self.wait(0.5)  # Reduced wait time
        self.play(Write(distance_formula))
        self.wait(1)  # Reduced wait time
        
        # Clear history section
        self.play(
            FadeOut(greek_math, euclid_label, pythagoras_theorem),
            FadeOut(modern_math, descartes_label, distance_formula),
            FadeOut(timeline, timeline_text, section_title)
        )
        
        # SECTION 2: PROPERTIES OF EUCLIDEAN DISTANCE - Fixed positioning
        section_title = Text("Properties of Euclidean Distance", font_size=36, color=PURPLE)
        section_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(section_title))
        self.wait(0.5)  # Reduced wait time
        
        # Property 1: ISOTROPIC (Same in all directions) - Fixed positioning
        prop1_title = Text("Isotropy: Equal in All Directions", font_size=28, color=TEAL)
        prop1_title.next_to(section_title, DOWN, buff=0.5)
        self.play(Write(prop1_title))
        
        # Create a circle visualization to show isotropy - better positioning
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-4, 4],
            axis_config={"include_numbers": True, "include_ticks": True},
            x_length=6,
            y_length=6,
            tips=False
        ).scale(0.7)
        
        # Position axes to avoid overlap with titles
        axes.next_to(prop1_title, DOWN, buff=0.5)
        
        # Create center point
        center_point = Dot(axes.coords_to_point(0, 0), color=RED, radius=0.1)
        center_label = Text("O", font_size=24, color=RED).next_to(center_point, DOWN+LEFT, buff=0.1)
        
        # Create distance circles with better labels
        circles = VGroup()
        circle_labels = VGroup()  # Separate group for labels to control their positioning
        
        for radius in [1, 2, 3]:
            circle = Circle(radius=radius, color=BLUE_A, stroke_opacity=0.7)
            circle.move_to(axes.coords_to_point(0, 0))
            circle.scale(axes.get_x_unit_size())  # Scale to match axes
            circles.add(circle)
            
            # Position label at 45° angle and ensure it's visible
            label_point = circle.point_at_angle(PI/4)
            circle_label = Text(f"d = {radius}", font_size=16, color=BLUE)
            circle_label.move_to(label_point + UP*0.2 + RIGHT*0.2)  # Fixed positioning
            circle_labels.add(circle_label)
        
        # Animate the isotropy visualization
        self.play(Create(axes))
        self.play(FadeIn(center_point), Write(center_label))
        self.wait(0.2)  # Reduced wait time
        
        for i in range(len(circles)):
            self.play(Create(circles[i]))
            self.play(Write(circle_labels[i]))
            self.wait(0.2)  # Reduced wait time
        
        # Show radial lines to emphasize equal distance in all directions
        lines = VGroup()
        angles = [0, PI/4, PI/2, 3*PI/4, PI, 5*PI/4, 3*PI/2, 7*PI/4]
        for angle in angles:
            end_point = axes.coords_to_point(3 * np.cos(angle), 3 * np.sin(angle))
            line = DashedLine(center_point.get_center(), end_point, color=YELLOW)
            lines.add(line)
        
        self.play(Create(lines))
        self.wait(0.7)  # Reduced wait time
        
        # Clear isotropy visualization
        self.play(
            FadeOut(axes, center_point, center_label),
            FadeOut(circles, circle_labels, lines),
            FadeOut(prop1_title)
        )
        
        # Property 3: EUCLIDEAN VS NON-EUCLIDEAN SPACES - Improved visualization
        prop3_title = Text("Euclidean vs. Non-Euclidean Geometry", font_size=28, color=GREEN)
        prop3_title.next_to(section_title, DOWN, buff=0.5)
        self.play(Write(prop3_title))
        
        # Create flat space vs curved space comparison with proper positioning
        flat_space_label = Text("Euclidean (Flat) Space", font_size=20, color=BLUE)
        flat_space_label.to_edge(LEFT, buff=2.5)
        flat_space_label.shift(UP * 0.5)
        
        curved_space_label = Text("Non-Euclidean (Curved) Space", font_size=20, color=RED)
        curved_space_label.to_edge(RIGHT, buff=2.5)
        curved_space_label.shift(UP * 0.5)
        
        self.play(Write(flat_space_label), Write(curved_space_label))
        self.wait(0.2)  # Reduced wait time
        
        flat_space = Square(side_length=3, color=BLUE, fill_opacity=0.2)
        flat_space.next_to(flat_space_label, DOWN, buff=0.3)
        
        # Create a grid on flat space
        flat_grid = VGroup()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                point = Dot(flat_space.get_center() + RIGHT*i + UP*j, color=YELLOW, radius=0.07)
                flat_grid.add(point)
        
        # Add center and a sample line
        flat_center = Dot(flat_space.get_center(), color=RED, radius=0.1)
        flat_sample = flat_grid[0]
        flat_line = Line(flat_center.get_center(), flat_sample.get_center(), color=GREEN)
        
        # Curved space (represented by a sphere)
        curved_space = Circle(radius=1.5, color=RED, fill_opacity=0.2)
        curved_space.next_to(curved_space_label, DOWN, buff=0.3)
        
        # Create points on the circle
        curved_grid = VGroup()
        for angle in np.linspace(0, 2*PI, 8, endpoint=False):
            point = Dot(curved_space.get_center() + 1.5 * RIGHT * np.cos(angle) + 1.5 * UP * np.sin(angle), 
                        color=YELLOW, radius=0.07)
            curved_grid.add(point)
        
        # Add center and geodesic
        curved_center = Dot(curved_space.get_center(), color=RED, radius=0.1)
        curved_sample = curved_grid[0]
        
        # Straight line (incorrect in curved space)
        wrong_line = Line(curved_center.get_center(), curved_sample.get_center(), color=GREEN)
        
        # Geodesic (correct in curved space) - ensure this is visible
        geodesic = Arc(
            radius=1.5,
            start_angle=0,
            angle=PI/4,  # Make this more visible
            color=PURPLE,
            stroke_width=4
        )
        geodesic.move_arc_center_to(curved_space.get_center())
        
        # Animate the space comparison
        self.play(
            Create(flat_space),
            Create(curved_space)
        )
        self.wait(0.5)  # Reduced wait time
        
        self.play(
            FadeIn(flat_center),
            FadeIn(curved_center),
            FadeIn(flat_grid),
            FadeIn(curved_grid)
        )
        self.wait(0.5)  # Reduced wait time
        
        self.play(Create(flat_line))
        self.play(Create(wrong_line))
        self.wait(0.5)  # Reduced wait time
        
        # Show the correct geodesic in curved space
        wrong_line_copy = wrong_line.copy().set_color(RED).set_opacity(0.5)
        self.play(Transform(wrong_line, wrong_line_copy))
        self.play(Create(geodesic))
        
        # Add explanation text with better positioning
        compare_text = Text("Shortest path changes in curved space!", font_size=22, color=YELLOW)
        compare_text.to_edge(DOWN, buff=0.8)  # Position at bottom with enough buffer
        self.play(Write(compare_text))
        self.wait(1)  # Reduced wait time
        
        # Clear space comparison
        self.play(
            FadeOut(flat_space, curved_space, flat_space_label, curved_space_label),
            FadeOut(flat_center, curved_center, flat_grid, curved_grid),
            FadeOut(flat_line, wrong_line, geodesic, compare_text),
            FadeOut(prop3_title)
        )
        
        # Clear property section
        self.play(FadeOut(section_title))
        
        # SECTION: HOW IT WORKS - FIXED positioning with NO calculation formula overlap
        section_title = Text("How It Works", font_size=36, color=GREEN)
        section_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(section_title))
        
        # Formula display with proper sizing
        formula = MathTex(
            r"\text{Distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}",
            font_size=34
        ).next_to(section_title, DOWN, buff=0.5)
        
        self.play(Write(formula))
        self.wait(1)  # Reduced wait time
        
        # Create coordinate system with better positioning
        axes = Axes(
            x_range=[-1, 6],
            y_range=[-1, 6],
            axis_config={"include_numbers": True},
            x_length=6,
            y_length=6,
            tips=False
        ).scale(0.7)
        
        # Position axes to not overlap with formula
        axes.next_to(formula, DOWN, buff=0.7)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)  # Reduced wait time
        
        # Plot points with more visual emphasis
        point_A = Dot(axes.coords_to_point(1, 1), color=BLUE, radius=0.12)
        label_A = Text("A(1, 1)", font_size=24, color=BLUE).next_to(point_A, DOWN+LEFT, buff=0.2)
        
        self.play(
            FadeIn(point_A, scale=1.5), 
            Write(label_A),
            Flash(point_A, color=BLUE, flash_radius=0.3)
        )
        self.wait(0.5)  # Reduced wait time
        
        point_B = Dot(axes.coords_to_point(4, 4), color=RED, radius=0.12)
        label_B = Text("B(4, 4)", font_size=24, color=RED).next_to(point_B, UP+RIGHT, buff=0.2)
        
        self.play(
            FadeIn(point_B, scale=1.5), 
            Write(label_B),
            Flash(point_B, color=RED, flash_radius=0.3)
        )
        self.wait(0.5)  # Reduced wait time
        
        # Draw components with proper labels
        x_line = Line(
            axes.coords_to_point(1, 1),
            axes.coords_to_point(4, 1),
            color=GREEN_B
        )
        y_line = Line(
            axes.coords_to_point(4, 1),
            axes.coords_to_point(4, 4),
            color=PURPLE_B
        )
        
        # Position labels to not overlap
        delta_x = MathTex(r"\Delta x = 3", font_size=24, color=GREEN_B)
        delta_x.next_to(x_line, DOWN, buff=0.2)
        
        delta_y = MathTex(r"\Delta y = 3", font_size=24, color=PURPLE_B)
        delta_y.next_to(y_line, RIGHT, buff=0.2)
        
        self.play(Create(x_line), Write(delta_x))
        self.wait(0.5)  # Reduced wait time
        self.play(Create(y_line), Write(delta_y))
        self.wait(0.7)  # Reduced wait time
        
        # Draw the hypotenuse with animation
        hypotenuse = Line(point_A.get_center(), point_B.get_center(), color=YELLOW)
        self.play(Create(hypotenuse))
        self.wait(0.5)  # Reduced wait time
        
        # Right angle indicator
        right_angle = RightAngle(x_line, y_line, quadrant=(-1, 1), length=0.25, color=WHITE)
        self.play(Create(right_angle))
        self.wait(0.5)  # Reduced wait time
        
        # Only showing the distance label next to point B
        distance_label = MathTex(r"d \approx 4.24", font_size=28, color=YELLOW)
        distance_label.next_to(point_B, RIGHT, buff=0.5)  # Better positioning
        self.play(
            hypotenuse.animate.set_stroke(width=6, color=YELLOW),
            Write(distance_label)
        )
        self.wait(1)  # Reduced wait time
        
        # Clear the diagram
        self.play(
            FadeOut(axes, axes_labels, point_A, point_B, label_A, label_B),
            FadeOut(hypotenuse, x_line, y_line, delta_x, delta_y, right_angle),
            FadeOut(distance_label, formula, section_title)
        )
        
                # NEW SECTION: K-NEAREST NEIGHBORS - COMPLETELY REDESIGNED TO FIX OVERLAPS
        section_title = Text("K-Nearest Neighbors Algorithm", font_size=36, color=BLUE_D)
        section_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(section_title))
        self.wait(0.5)  # Short wait time

        # Subtitle explaining the concept - moved closer to title for better spacing
        subtitle = Text("Classification using distance-based similarity", font_size=24)
        subtitle.next_to(section_title, DOWN, buff=0.4)
        self.play(Write(subtitle))
        self.wait(0.7)  # Short wait time

        # IMPORTANT: Fade out the title and subtitle before showing the graph
        # This prevents the graph from overlapping with the text
        self.play(FadeOut(section_title), FadeOut(subtitle))
        self.wait(0.3)

        # Create a coordinate system for KNN with appropriate dimensions
        # Making axis larger and positioned at the center of the screen
        knn_axes = Axes(
            x_range=[0, 7],  # Start from 0 to avoid negative area
            y_range=[0, 7],  # Start from 0 to avoid negative area
            axis_config={"include_numbers": True, "numbers_to_include": range(1, 8)},
            x_length=7,      # Slightly larger for better visibility
            y_length=7,      # Slightly larger for better visibility
            tips=False
        ).scale(0.75)

        # Position axes at the center of the screen
        knn_axes.center()    # This centers the axes in the screen

        # Clear axis labels
        x_label = Text("Feature 1", font_size=20).next_to(knn_axes, DOWN, buff=0.15)
        y_label = Text("Feature 2", font_size=20).next_to(knn_axes, LEFT, buff=0.15).rotate(PI/2)

        self.play(Create(knn_axes))
        self.play(Write(x_label), Write(y_label))
        self.wait(0.3)

        # Set fixed seed for deterministic point positions
        np.random.seed(42)

        # Generate class A points (blue cluster) in the bottom left
        class_a_points = VGroup()
        for i in range(6):  # Fewer points to reduce clutter
            x = np.random.uniform(1.0, 2.5)  # Moved a bit left
            y = np.random.uniform(1.8, 3.0)  # Limited y-range to avoid overlaps
            point = Dot(knn_axes.coords_to_point(x, y), color=BLUE, radius=0.08)
            class_a_points.add(point)

        # Generate class B points (red cluster) in the top right
        class_b_points = VGroup()
        for i in range(6):  # Fewer points to reduce clutter
            x = np.random.uniform(4.2, 5.8)  # Moved a bit right
            y = np.random.uniform(3.8, 5.0)  # Adjusted y-range
            point = Dot(knn_axes.coords_to_point(x, y), color=RED, radius=0.08)
            class_b_points.add(point)

        # Add all points at once for efficiency
        self.play(FadeIn(class_a_points), FadeIn(class_b_points))

        # Place the query point in a location that won't cause diagonal lines across text
        query_point = Dot(knn_axes.coords_to_point(3.5, 3.5), color=GREEN, radius=0.12)
        query_label = Text("?", font_size=22, color=GREEN).next_to(query_point, UP, buff=0.15)  # Label above

        self.play(
            FadeIn(query_point, scale=1.5),
            Write(query_label),
            Flash(query_point, color=GREEN, flash_radius=0.3)
        )
        self.wait(0.5)

        # Use very specific positions for nearest neighbors to avoid text-crossing lines
        nearest_1 = Dot(knn_axes.coords_to_point(2.8, 2.9), color=BLUE, radius=0.09)  # Blue point (bottom left)
        nearest_2 = Dot(knn_axes.coords_to_point(3.8, 3.8), color=RED, radius=0.09)   # Red point (top right)
        nearest_3 = Dot(knn_axes.coords_to_point(4.2, 3.5), color=RED, radius=0.09)   # Red point (right)

        # Add these specific points to our scene
        self.play(FadeIn(nearest_1), FadeIn(nearest_2), FadeIn(nearest_3))

        # Draw distance lines with good visibility - carefully positioned
        distance_lines = VGroup()
        for point in [nearest_1, nearest_2, nearest_3]:
            line = DashedLine(
                query_point.get_center(),
                point.get_center(),
                color=YELLOW,
                stroke_width=1.5,
                stroke_opacity=0.7
            )
            distance_lines.add(line)

        self.play(Create(distance_lines))
        self.wait(0.3)

        # Highlight the 3 nearest neighbors
        nearest_circles = VGroup()
        for point in [nearest_1, nearest_2, nearest_3]:
            circle = Circle(radius=0.2, color=YELLOW, stroke_width=2)
            circle.move_to(point.get_center())
            nearest_circles.add(circle)

        self.play(Create(nearest_circles))
        self.wait(0.5)

        # Add class label for clarity
        class_b_indicator = Text("B", font_size=18, color=RED)
        class_b_indicator.move_to(nearest_2.get_center()).shift(UP * 0.25 + RIGHT * 0.25)
        self.play(Write(class_b_indicator))
        self.wait(0.2)

        # Add explanatory text near the bottom of screen but not directly under lines
        k_text = Text("K=3: considering only 3 nearest neighbors", font_size=20, color=YELLOW)
        k_text.to_edge(DOWN, buff=0.4)
        self.play(Write(k_text))
        self.wait(0.3)

        # Show the classification result
        self.play(FadeOut(x_label))
        result_text = Text("Classification by majority: 2 red, 1 blue → Class B", font_size=22, color=YELLOW)
        result_text.next_to(k_text, UP, buff=0.2)
        self.play(Write(result_text))

        # Assign query point to Class B
        self.play(
            query_point.animate.set_color(RED),
            query_label.animate.become(
                Text("B", font_size=22, color=RED).next_to(query_point, UP, buff=0.15)  # Keep label above
            )
        )
        self.wait(0.5)

        # Clear KNN visualization
        self.play(
            FadeOut(knn_axes, x_label, y_label),
            FadeOut(class_a_points, class_b_points),
            FadeOut(query_point, query_label, nearest_1, nearest_2, nearest_3, class_b_indicator),
            FadeOut(distance_lines, nearest_circles, k_text, result_text)
        )

        # Show title again for the next section
        section_title = Text("Real-World Example: Stock Trading", font_size=36, color=ORANGE)
        section_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(section_title))
        self.wait(0.5)  # Reduced wait time
        
        # PART 1: DATA COMPARISON WITH CLEAR POSITIONING
        # Introduction to pairs trading concept
        intro_text = Text(
            "Pairs Trading Strategy: Finding Correlated Stocks",
            font_size=26
        ).next_to(section_title, DOWN, buff=0.5)
        self.play(Write(intro_text))
        self.wait(0.7)  # Reduced wait time
        
        # Create stock table with improved spacing
        days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        stock_A_returns = [1.2, 0.8, -0.5, 1.4, -0.2]  # Coca-Cola
        stock_B_returns = [1.0, 0.5, -0.8, 1.0, 0.3]   # Pepsi
        
        table = Table(
            [["Day"] + days,
             ["Coca-Cola"] + [f"{x}%" for x in stock_A_returns],
             ["Pepsi"] + [f"{x}%" for x in stock_B_returns]],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
            v_buff=0.3,
            h_buff=0.6
        ).scale(0.6)
        
        # Position table to leave room for the graph
        table.next_to(intro_text, DOWN, buff=0.5)
        self.play(Create(table))
        self.wait(1)  # Reduced wait time
        
        # Calculate Euclidean distance first
        distance_title = Text("Calculating Euclidean Distance:", font_size=24)
        distance_title.next_to(table, DOWN, buff=0.7)
        
        distance_formula = MathTex(
            r"d = \sqrt{\sum_{i=1}^{5} (A_i - B_i)^2} \approx 0.79",
            font_size=28
        ).next_to(distance_title, DOWN, buff=0.3)
        
        self.play(Write(distance_title))
        self.play(Write(distance_formula))
        self.wait(1)  # Reduced wait time
        
        # Clear for visualization
        self.play(FadeOut(table, distance_title, distance_formula))
        
        # PART 2: STOCK RETURN VISUALIZATION - PROPERLY POSITIONED
        # Create stock return graph
        returns_title = Text("Visualizing Stock Returns", font_size=26)
        returns_title.next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(returns_title))
        
        axes = Axes(
            x_range=[0, 6],
            y_range=[-1.5, 2],
            axis_config={"include_numbers": True},
            x_length=8,
            y_length=4,
            tips=False
        ).scale(0.65)
        
        # Ensure proper positioning - center on screen
        axes.next_to(returns_title, DOWN, buff=0.5)
        
        # Clear axis labels
        x_label = Text("Day", font_size=20).next_to(axes, DOWN, buff=0.2)
        y_label = Text("Return %", font_size=20).next_to(axes, LEFT, buff=0.2).rotate(PI/2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)  # Reduced wait time
        
        # Plot stock lines with better visibility
        days_positions = range(1, 6)
        stock_A_points = [axes.coords_to_point(i, stock_A_returns[i-1]) for i in days_positions]
        stock_B_points = [axes.coords_to_point(i, stock_B_returns[i-1]) for i in days_positions]
        
        # Create dots for each data point
        stock_A_dots = VGroup(*[Dot(point, color=BLUE, radius=0.08) for point in stock_A_points])
        stock_B_dots = VGroup(*[Dot(point, color=RED, radius=0.08) for point in stock_B_points])
        
        # Create lines connecting the dots
        stock_A_line = VMobject()
        stock_A_line.set_points_as_corners(stock_A_points)
        stock_A_line.set_color(BLUE)
        
        stock_B_line = VMobject()
        stock_B_line.set_points_as_corners(stock_B_points)
        stock_B_line.set_color(RED)
        
        # Create labels for the lines - position to avoid overlap
        stock_A_label = Text("Coca-Cola", font_size=20, color=BLUE).next_to(stock_A_points[-1], UR, buff=0.2)
        stock_B_label = Text("Pepsi", font_size=20, color=RED).next_to(stock_B_points[-1], DR, buff=0.2)
        
        # Animate creation of graph elements
        self.play(Create(stock_A_line), Create(stock_B_line))
        self.play(FadeIn(stock_A_dots), FadeIn(stock_B_dots))
        self.play(Write(stock_A_label), Write(stock_B_label))
        self.wait(1)  # Reduced wait time
        
        # Euclidean distance result displayed below
        distance_result = Text("Low Euclidean Distance (0.79) = High Correlation", font_size=24, color=YELLOW)
        distance_result.to_edge(DOWN, buff=1.0)
        self.play(Write(distance_result))
        self.wait(1)  # Reduced wait time
        
        # Clear for trading strategy
        self.play(
            FadeOut(returns_title, axes, x_label, y_label),
            FadeOut(stock_A_line, stock_B_line, stock_A_dots, stock_B_dots),
            FadeOut(stock_A_label, stock_B_label, distance_result)
        )
        
        # PART 3: TRADING STRATEGY - CLEAR SEQUENTIAL STEPS
        strategy_title = Text("Trading Strategy Based on Correlation", font_size=28, color=GREEN)
        strategy_title.next_to(intro_text, DOWN, buff=0.5)
        self.play(Write(strategy_title))
        self.wait(0.5)  # Reduced wait time
        
        # STEP 1: Clear visualization
        step1_text = Text("Step 1: Identify correlated stocks using Euclidean Distance", font_size=24)
        step1_text.next_to(strategy_title, DOWN, buff=0.5)
        self.play(Write(step1_text))
        
        # Simple visualization showing correlation
        step1_dots = VGroup()
        # First stock path
        path1_points = []
        for i in range(6):
            x = i
            y = 0.5 * np.sin(i*0.8) + 1.5
            path1_points.append([x, y, 0])
            
        # Second stock path - similar pattern
        path2_points = []
        for i in range(6):
            x = i
            y = 0.5 * np.sin(i*0.8) + 1.2  # Just offset slightly
            path2_points.append([x, y, 0])
        
        # Create lines
        stock1_line = VMobject()
        stock1_line.set_points_smoothly(path1_points)
        stock1_line.set_color(BLUE)
        
        stock2_line = VMobject()
        stock2_line.set_points_smoothly(path2_points)
        stock2_line.set_color(RED)
        
        correlation_viz = VGroup(stock1_line, stock2_line)
        correlation_viz.scale(0.7).next_to(step1_text, DOWN, buff=0.5)
        
        corr_label1 = Text("Coca-Cola", font_size=18, color=BLUE).next_to(correlation_viz, UL, buff=0.2)
        corr_label2 = Text("Pepsi", font_size=18, color=RED).next_to(correlation_viz, DL, buff=0.2)
        
        self.play(Create(stock1_line), Create(stock2_line))
        self.play(Write(corr_label1), Write(corr_label2))
        self.wait(1)  # Reduced wait time
        
        # Clear step 1
        self.play(
            FadeOut(step1_text, correlation_viz, corr_label1, corr_label2)
        )
        
        # STEP 2: Monitor price ratio
        step2_text = Text("Step 2: Monitor price ratio between correlated stocks", font_size=24)
        step2_text.next_to(strategy_title, DOWN, buff=0.5)
        self.play(Write(step2_text))
        
        # Create visualization of price ratio - NUMBER LINE ONLY
        ratio_axis = NumberLine(
            x_range=[0.7, 1.1, 0.1],
            length=6,
            include_numbers=True,
            numbers_to_include=[0.7, 0.8, 0.9, 1.0, 1.1]
        ).scale(0.8)
        
        ratio_label = Text("Coca-Cola/Pepsi Price Ratio", font_size=20)
        ratio_label.next_to(ratio_axis, UP, buff=0.3)
        
        # Position the entire ratio visualization
        ratio_viz = VGroup(ratio_axis, ratio_label)
        ratio_viz.next_to(step2_text, DOWN, buff=0.5)
        
        self.play(Create(ratio_axis), Write(ratio_label))
        self.wait(0.5)  # Reduced wait time
        
        # Add markers with clear spacing
        avg_marker = Triangle().scale(0.2).set_color(GREEN)
        avg_marker.next_to(ratio_axis.n2p(0.85), DOWN, buff=0.1)
        avg_label = Text("Historical Average", font_size=16, color=GREEN)
        avg_label.next_to(avg_marker, DOWN, buff=0.3)
        
        deviation_marker = Triangle().scale(0.2).set_color(RED)
        deviation_marker.next_to(ratio_axis.n2p(0.72), DOWN, buff=0.1)
        deviation_label = Text("Deviation", font_size=16, color=RED)
        deviation_label.next_to(deviation_marker, DOWN, buff=0.3)
        
        self.play(FadeIn(avg_marker), Write(avg_label))
        self.wait(0.5)  # Reduced wait time
        self.play(FadeIn(deviation_marker), Write(deviation_label))
        self.wait(0.7)  # Reduced wait time
        
        # Clear step 2
        self.play(
            FadeOut(step2_text, ratio_viz, avg_marker, avg_label, deviation_marker, deviation_label)
        )
        
        # STEP 3: Trade on deviation
        step3_text = Text("Step 3: When ratio deviates, buy undervalued and sell overvalued stock", font_size=24)
        step3_text.next_to(strategy_title, DOWN, buff=0.5)
        self.play(Write(step3_text))
        
        # Trading action visualization
        trade_box = VGroup(
            SurroundingRectangle(
                VGroup(
                    Text("Buy Coca-Cola", font_size=20, color=BLUE),
                    Text("(Undervalued)", font_size=18, color=BLUE_A)
                ).arrange(DOWN, buff=0.1),
                color=GREEN_B,
                buff=0.3
            ),
            SurroundingRectangle(
                VGroup(
                    Text("Sell Pepsi", font_size=20, color=RED),
                    Text("(Overvalued)", font_size=18, color=RED_A)
                ).arrange(DOWN, buff=0.1),
                color=RED_B,
                buff=0.3
            )
        ).arrange(RIGHT, buff=1.0).next_to(step3_text, DOWN, buff=0.5)
        
        self.play(Create(trade_box))
        self.wait(1)  # Reduced wait time
        
        # Clear step 3
        self.play(FadeOut(step3_text, trade_box))
        
        # STEP 4: Profit from mean reversion
        step4_text = Text("Step 4: Profit when ratio returns to historical average", font_size=24)
        step4_text.next_to(strategy_title, DOWN, buff=0.5)
        self.play(Write(step4_text))
        
        # Create new ratio number line for profit visualization
        profit_axis = NumberLine(
            x_range=[0.7, 1.1, 0.1],
            length=6,
            include_numbers=True,
            numbers_to_include=[0.7, 0.8, 0.9, 1.0, 1.1]
        ).scale(0.8)
        
        profit_label = Text("Price Ratio Movement", font_size=20)
        profit_label.next_to(profit_axis, UP, buff=0.3)
        
        profit_viz = VGroup(profit_axis, profit_label)
        profit_viz.next_to(step4_text, DOWN, buff=0.5)
        
        self.play(Create(profit_axis), Write(profit_label))
        
        # Add markers again
        p_start_marker = Triangle().scale(0.2).set_color(RED)
        p_start_marker.next_to(profit_axis.n2p(0.72), DOWN, buff=0.1)
        p_start_label = Text("Entry Point", font_size=16, color=RED)
        p_start_label.next_to(p_start_marker, DOWN, buff=0.3)
        
        p_end_marker = Triangle().scale(0.2).set_color(GREEN)
        p_end_marker.next_to(profit_axis.n2p(0.85), DOWN, buff=0.1)
        p_end_label = Text("Exit Point", font_size=16, color=GREEN)
        p_end_label.next_to(p_end_marker, DOWN, buff=0.3)
        
        self.play(FadeIn(p_start_marker), Write(p_start_label))
        self.play(FadeIn(p_end_marker), Write(p_end_label))
        
        # Create profit arrow with clear positioning
        profit_arrow = Arrow(
            profit_axis.n2p(0.72) + DOWN*0.5, 
            profit_axis.n2p(0.85) + DOWN*0.5, 
            color=GREEN_B, 
            buff=0
        )
        profit_label = Text("Profit Zone", font_size=20, color=GREEN)
        profit_label.next_to(profit_arrow, DOWN, buff=0.3)
        
        self.play(Create(profit_arrow))
        self.play(Write(profit_label))
        self.wait(1)  # Reduced wait time
        
        # Emphasize the key insight at bottom with clear spacing
        key_insight = Text(
            "Key Insight: Euclidean Distance identifies mathematical relationships\nthat can be exploited for trading profit",
            font_size=24,
            color=YELLOW
        )
        key_insight.to_edge(DOWN, buff=0.5)  # Increased buffer to prevent overlap
        
        self.play(Write(key_insight))
        self.wait(1)  # Reduced wait time
        
        # Clear everything for conclusion
        self.play(
            FadeOut(intro_text, strategy_title, step4_text),
            FadeOut(profit_viz, p_start_marker, p_start_label),
            FadeOut(p_end_marker, p_end_label, profit_arrow, profit_label),
            FadeOut(key_insight)
        )
        
        # CONCLUSION - FIXED WITH SIMPLE BULLET POINTS
        conclusion_title = Text("Key Takeaways", font_size=36, color=PURPLE)
        conclusion_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(conclusion_title))
        self.wait(0.5)  # Reduced wait time
        
        # Simple bullet points instead of complex visuals
        takeaways = [
            "Simple Formula: Easy to calculate and understand",
            "Real-World Applications: Powerful tool in finance and data analysis",
            "Mathematical Foundation: Basis for more advanced distance metrics",
            "Pattern Discovery: Reveals hidden relationships in complex data",
            "Trading Strategy: Enables statistical arbitrage and pairs trading"
        ]
        
        bullet_points = VGroup()
        for i, point in enumerate(takeaways):
            bullet = Text("•", font_size=28, color=YELLOW).shift(LEFT * 3.5 + DOWN * (i * 0.7 + 0.5))
            text = Text(point, font_size=24).next_to(bullet, RIGHT, buff=0.3)
            bullet_points.add(VGroup(bullet, text))
        
        # Show each bullet point with adequate spacing
        for point in bullet_points:
            self.play(Write(point))
            self.wait(0.7)  # Reduced wait time
        
        # Final statement with emphasis - CLEAR POSITIONING
        final_text = Text(
            "Euclidean Distance: A powerful tool for discovering\nhidden patterns in financial data",
            font_size=28,
            color=YELLOW
        ).to_edge(DOWN, buff=0.7)
        
        self.play(Write(final_text))
        self.wait(1)  # Reduced wait time
        
        # Final fade out
        self.play(FadeOut(
            title, conclusion_title, 
            bullet_points,
            final_text
        ))
        
        # End screen
        final_title = Text(
            "Euclidean Distance in Finance",
            font_size=48,
            color=BLUE
        ).center()
        
        next_up = Text(
            "Next: Manhattan Distance & Other Metrics",
            font_size=32,
            color=GREEN
        ).next_to(final_title, DOWN, buff=1.0)
        
        self.play(Write(final_title))
        self.wait(0.5)  # Reduced wait time
        self.play(Write(next_up))
        self.wait(1)  # Reduced wait time