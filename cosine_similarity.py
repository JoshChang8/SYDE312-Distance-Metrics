from manim import *

class CosineSimilarityTitle(Scene):
    def construct(self):
        # Scene 1: Title
        title = Text("Cosine Similarity", font_size=72)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))


class CosineSimilarityIntuition(Scene):
    def construct(self):     
        # Create the explanation text
        explanation = Text("Compares the direction of two vectors", font_size=32)
        explanation.to_edge(UP, buff=1.5)
        
        # Set up the coordinate system
        axes = Axes(
            x_range=[-0.5, 3.5, 1],
            y_range=[-0.5, 3.5, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": False, "include_ticks": False},
        )
        axes.shift(DOWN * 0.5)  
        
        # Define angles for the animation sequence
        angles = [80, 60, 40]  # Start with 80 degrees, then decrease
        current_angle = angles[0]  # Start angle
        
        # Vector A is always along the x-axis 
        vec_A = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(2.2, 0), 
                     buff=0, color=BLUE, max_tip_length_to_length_ratio=0.15)
        label_A = MathTex(r"\vec{A}").next_to(vec_A.get_end(), RIGHT)
        
        # Vector B starts at the larger angle 
        end_x = 2.2 * np.cos(np.radians(current_angle))
        end_y = 2.2 * np.sin(np.radians(current_angle))
        vec_B = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(end_x, end_y), 
                     buff=0, color=GREEN, max_tip_length_to_length_ratio=0.15)
        label_B = MathTex(r"\vec{B}").next_to(vec_B.get_end(), UP + RIGHT)
        
        # Create angle arc and label
        angle_arc = Arc(
            radius=0.7,
            start_angle=0,
            angle=np.radians(current_angle),
            color=YELLOW,
            arc_center=axes.coords_to_point(0, 0)
        )
        
        # Position theta label outside the angle
        angle_label = MathTex(r"\theta", color=YELLOW)
        angle_label.scale(0.8)
        # Position outside the arc by using a larger radius
        angle_position = axes.coords_to_point(
            0.9 * np.cos(np.radians(current_angle/2)), 
            0.9 * np.sin(np.radians(current_angle/2))
        )
        angle_label.move_to(angle_position)
        
        # Create a static dot at the origin to visually verify vectors share same origin
        origin_dot = Dot(axes.coords_to_point(0, 0), color=RED, radius=0.05)
        
        # Animation sequence - faster pace for ~12s total duration
        self.play(Write(explanation), run_time=1)
        
        # Create vectors, angle visualization, and origin dot together
        self.play(
            Create(vec_A), 
            Create(label_A),
            Create(vec_B), 
            Create(label_B),
            Create(angle_arc), 
            Write(angle_label),
            Create(origin_dot),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Animate vector B decreasing in angle relative to vector A
        for i in range(1, len(angles)):
            target_angle = angles[i]
            
            # Calculate new end point for vector B - smaller vectors
            new_end_x = 2.2 * np.cos(np.radians(target_angle))
            new_end_y = 2.2 * np.sin(np.radians(target_angle))
            
            # Create new vector B
            new_vec_B = Arrow(
                axes.coords_to_point(0, 0), 
                axes.coords_to_point(new_end_x, new_end_y),  
                buff=0, 
                color=GREEN, 
                max_tip_length_to_length_ratio=0.15
            )
            
            # Create new label B
            new_label_B = MathTex(r"\vec{B}")
            new_label_B.next_to(new_vec_B.get_end(), UP + RIGHT)
            
            # Create new angle arc
            new_angle_arc = Arc(
                radius=0.7,
                start_angle=0,
                angle=np.radians(target_angle),
                color=YELLOW,
                arc_center=axes.coords_to_point(0, 0)
            )
            
            # New position for theta label - outside the arc
            new_angle_position = axes.coords_to_point(
                0.9 * np.cos(np.radians(target_angle/2)), 
                0.9 * np.sin(np.radians(target_angle/2))
            )
            new_angle_label = MathTex(r"\theta", color=YELLOW)
            new_angle_label.scale(0.8)
            new_angle_label.move_to(new_angle_position)
            
            # Animate the transition
            self.play(
                ReplacementTransform(vec_B, new_vec_B),
                ReplacementTransform(label_B, new_label_B),
                ReplacementTransform(angle_arc, new_angle_arc),
                ReplacementTransform(angle_label, new_angle_label),
                run_time=1.5
            )
            
            # Update references for next iteration
            vec_B = new_vec_B
            label_B = new_label_B
            angle_arc = new_angle_arc
            angle_label = new_angle_label
            
            # Brief pause to observe the new angle
            self.wait(0.5)
        
        # Final wait and fade out
        self.wait(1)
        self.play(
            FadeOut(explanation), 
            FadeOut(vec_A), 
            FadeOut(vec_B), 
            FadeOut(label_A), 
            FadeOut(label_B), 
            FadeOut(angle_arc), 
            FadeOut(angle_label),
            FadeOut(origin_dot),
            run_time=1
        )


class CosineSimilarityFormula(Scene):
    def construct(self):
        # Scene 3: Show the formula and break it down 
        formula = MathTex(
            r"\text{Cosine Similarity}", 
            r"=", 
            r"\cos(\theta)", 
            r"=",
            r"\frac{A\cdot B}{\|A\|\cdot\|B\|}"
        )
        
        # Center the formula in the middle of the screen
        formula.scale(1.2)
        formula.move_to(ORIGIN)  # Center in the middle of the screen
        
        # Initial display of the formula
        self.play(Write(formula))
        self.wait(1)  # Shorter pause
          
        # Highlight the cosine theta part
        cosine_theta_box = SurroundingRectangle(formula[2], color=YELLOW, buff=0.2)
        self.play(Create(cosine_theta_box))
        self.wait(1)  # Shorter pause
        self.play(FadeOut(cosine_theta_box))
        
        # Highlight the dot product in the numerator
        dot_product_box = SurroundingRectangle(formula[4][0:3], color=BLUE, buff=0.2)  # A·B part
        self.play(Create(dot_product_box))
        self.wait(1)  # Shorter pause
        self.play(FadeOut(dot_product_box))
        
        # Highlight the magnitudes in the denominator
        magnitudes_box = SurroundingRectangle(formula[4][4:], color=GREEN, buff=0.2)  # ||A||·||B|| part
        self.play(Create(magnitudes_box))
        self.wait(1)  # Shorter pause
        self.play(FadeOut(magnitudes_box))
        
        self.wait(1)  
        self.play(FadeOut(formula))


class CosineSimilarityExample(Scene):
    def construct(self):
        # Scene 4: Example 
        
        vec_A_value = [1, 2]
        vec_B_value = [3, 4]
        
        vec_info_group = VGroup()
        vec_A_label = MathTex(r"\vec{A} = [1, 2]", font_size=36)
        vec_B_label = MathTex(r"\vec{B} = [3, 4]", font_size=36)
        vec_B_label.next_to(vec_A_label, DOWN, aligned_edge=LEFT)
        vec_info_group.add(vec_A_label, vec_B_label)
        vec_info_group.to_corner(UL, buff=0.5)
        
        # Create coordinate system for the vector visualization in the center
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-1, 5],
            x_length=5,
            y_length=5,
            axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Create the vectors
        vec_A_arrow = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(vec_A_value[0], vec_A_value[1]), 
                          buff=0, color=BLUE, max_tip_length_to_length_ratio=0.15)
        vec_B_arrow = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(vec_B_value[0], vec_B_value[1]), 
                          buff=0, color=GREEN, max_tip_length_to_length_ratio=0.15)
        
        # Add vector labels to the arrows
        vec_A_arrow_label = MathTex(r"\vec{A}", color=BLUE).next_to(vec_A_arrow.get_end(), RIGHT+UP, buff=0.1)
        vec_B_arrow_label = MathTex(r"\vec{B}", color=GREEN).next_to(vec_B_arrow.get_end(), RIGHT+UP, buff=0.1)
        
        # Group the coordinate system and vectors (without angle indicator)
        vector_vis_group = VGroup(axes, axes_labels, vec_A_arrow, vec_B_arrow, 
                                 vec_A_arrow_label, vec_B_arrow_label)
        
        # Position the visualization below the vector definitions on the left side
        vector_vis_group.scale(0.9)  
        vector_vis_group.next_to(vec_info_group, DOWN, buff=0.5)
        vector_vis_group.to_edge(LEFT, buff=1)
        
        # Define fixed position for all calculations (to the right of the graph but not too far right)
        calc_position = RIGHT * 2.8 + DOWN * 0.5
        
        # Step 1: Dot product calculation with intermediate step
        dot_product = MathTex(
            r"\text{\small Dot Product:}" + \
            r"\\" + \
            r"A \cdot B &= (1 \times 3) + (2 \times 4)" + \
            r"\\" + \
            r"&= 3 + 8" + \
            r"\\" + \
            r"&= 11"
        )
        dot_product.scale(0.9)  
        dot_product.move_to(calc_position)
        
        # Step 2: Magnitude calculations with A above B
        magnitudes = MathTex(
            r"\text{\small Magnitudes:}" + \
            r"\\" + \
            r"\|A\| &= \sqrt{1^2+2^2} = \sqrt{5}" + \
            r"\\" + \
            r"\|B\| &= \sqrt{3^2+4^2} = \sqrt{25} = 5"
        )
        magnitudes.scale(0.9) 
        magnitudes.move_to(calc_position)
        
        # Step 3: Final calculation
        cosine_calc = MathTex(
            r"\text{\small Cosine Similarity:}" + \
            r"\\" + \
            r"\cos(\theta) &= \frac{A \cdot B}{\|A\| \cdot \|B\|}" + \
            r"\\" + \
            r"&= \frac{11}{\sqrt{5} \cdot 5}" + \
            r"\\" + \
            r"&= \frac{11}{5\sqrt{5}}" + \
            r"\\" + \
            r"&\approx 0.983"
        )
        cosine_calc.scale(0.9) 
        cosine_calc.move_to(calc_position)
        
        # Create the cosine similarity formula to be shown at the top after graph generation
        cos_sim_formula = MathTex(
            r"\text{Cosine Similarity} = \cos(\theta) = \frac{A \cdot B}{\|A\| \cdot \|B\|}"
        )
        cos_sim_formula.scale(0.9) 
        cos_sim_formula.to_edge(UP, buff=0.5)
        
        # Animation sequence
        # 1. Show vector definitions
        self.play(Write(vec_info_group))
        self.wait(0.5)
        
        # 2. Create the coordinate system and vectors
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)
        self.play(Create(vec_A_arrow), Write(vec_A_arrow_label))
        self.wait(0.2)
        self.play(Create(vec_B_arrow), Write(vec_B_arrow_label))
        self.wait(1)
        
        # 3. Display the cosine similarity formula at the top
        self.play(Write(cos_sim_formula))
        self.wait(1)
        
        # 4. Step by step calculations, each in the same position
        # First: Dot Product
        self.play(Write(dot_product))
        self.wait(2)
        self.play(FadeOut(dot_product))
        
        # Second: Magnitudes
        self.play(Write(magnitudes))
        self.wait(3)
        self.play(FadeOut(magnitudes))
        
        # Third: Final Cosine Similarity calculation
        self.play(Write(cosine_calc))
        self.wait(4)
        
        # Fade out everything
        self.play(FadeOut(vec_info_group, vector_vis_group, cos_sim_formula, cosine_calc))


class CosineSimilarityInterpretation(Scene):
    def construct(self):
        # Scene 5: Visual Interpretation of Cosine Similarity (not included due to time constraints)
        
        grid_width = 2.5
        grid_height = 2.5
        
        # Scenario 1: Vectors pointing in same direction (cos≈1)
        axes1 = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            x_length=grid_width,
            y_length=grid_height,
            axis_config={"include_tip": True, "include_numbers": False}
        )
        
        # Scenario 2: Vectors at 90° to each other (cos≈0)
        axes2 = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            x_length=grid_width,
            y_length=grid_height,
            axis_config={"include_tip": True, "include_numbers": False}
        )
        
        # Scenario 3: Vectors pointing in opposite directions (cos≈-1)
        axes3 = Axes(
            x_range=[-2, 2],
            y_range=[-2, 2],
            x_length=grid_width,
            y_length=grid_height,
            axis_config={"include_tip": True, "include_numbers": False}
        )
        
        # Position the three axes in a row
        axes_group = VGroup(axes1, axes2, axes3).arrange(RIGHT, buff=1.5)
        axes_group.to_edge(UP, buff=1.0)
        
        # Create vector pairs for each scenario
        # Scenario 1: Same direction
        vec1_a = Arrow(axes1.coords_to_point(0, 0), axes1.coords_to_point(1.5, 1), buff=0, color=RED, max_tip_length_to_length_ratio=0.15)
        vec1_b = Arrow(axes1.coords_to_point(0, 0), axes1.coords_to_point(1.2, 0.8), buff=0, color=RED, max_tip_length_to_length_ratio=0.15)
        
        # Scenario 2: Perpendicular (90°)
        vec2_a = Arrow(axes2.coords_to_point(0, 0), axes2.coords_to_point(1.5, 0), buff=0, color=RED, max_tip_length_to_length_ratio=0.15)
        vec2_b = Arrow(axes2.coords_to_point(0, 0), axes2.coords_to_point(0, 1.5), buff=0, color=RED, max_tip_length_to_length_ratio=0.15)
        
        # Scenario 3: Opposite directions
        vec3_a = Arrow(axes3.coords_to_point(0, 0), axes3.coords_to_point(1.5, 0.5), buff=0, color=RED, max_tip_length_to_length_ratio=0.15)
        vec3_b = Arrow(axes3.coords_to_point(0, 0), axes3.coords_to_point(-1.2, -0.4), buff=0, color=RED, max_tip_length_to_length_ratio=0.15)
        
        # Create labels for each scenario
        label1 = Tex("Angle is close to 0\\\\", "Cos($\\theta$) close to 1\\\\", "Similar vectors", font_size=24)
        label1.arrange(DOWN, aligned_edge=LEFT)
        label1.next_to(axes1, DOWN, buff=0.5)
        
        label2 = Tex("Angle is close to 90$^\\circ$\\\\", "Cos($\\theta$) close to 0\\\\", "Unrelated vectors", font_size=24)
        label2.arrange(DOWN, aligned_edge=LEFT)
        label2.next_to(axes2, DOWN, buff=0.5)
        
        label3 = Tex("Angle is close to 180$^\\circ$\\\\", "Cos($\\theta$) close to -1\\\\", "Opposite vectors", font_size=24)
        label3.arrange(DOWN, aligned_edge=LEFT)
        label3.next_to(axes3, DOWN, buff=0.5)
        
        # Show the grids first
        self.play(Create(axes1), Create(axes2), Create(axes3))
        self.wait(1)
        
        # Show the vectors in each scenario
        self.play(
            Create(vec1_a), Create(vec1_b),
            Create(vec2_a), Create(vec2_b),
            Create(vec3_a), Create(vec3_b)
        )
        self.wait(1)
        
        # Show the labels
        self.play(Write(label1), Write(label2), Write(label3))
        self.wait(3)
        
        # Fade out everything
        self.play(FadeOut(VGroup(axes1, axes2, axes3, 
                          vec1_a, vec1_b, vec2_a, vec2_b, vec3_a, vec3_b,
                          label1, label2, label3)))


class CosineSimilarityMusicRec(Scene):
    def construct(self):
        # Scene 5: Music Recommendation Example
        title = Text("Cosine Similarity for Recommendation Systems", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Show a vector with 5 elements corresponding to music features
        features = ["Tempo", "Energy", "Danceability", "Instrumentation", "Vocals"]
        feature_values = [0.8, 0.7, 0.9, 0.4, 0.6]  # Example values
        
        # Create feature vector visualization in the center
        vector_title = Text("Song As A Feature Vector", font_size=40, slant=ITALIC)
        vector_title.next_to(title, DOWN, buff=0.7)
        self.play(Write(vector_title))
        
        # Create numerical vector representation with similar styling to image
        numerical_vector = Text(
            "[ 0.8 , 0.7 , 0.9 , 0.4 , 0.6 ]", 
            font_size=48
        )
        numerical_vector.next_to(vector_title, DOWN, buff=1)
        self.play(Write(numerical_vector))
        
        # Position feature names and draw arrows to numerical values
        feature_labels = VGroup()
        arrows = VGroup()
        
        # Calculate positions for each feature value
        vector_width = numerical_vector.width
        value_positions = [
            numerical_vector.get_center() + np.array([-vector_width*0.36, 0, 0]),  # 0.8
            numerical_vector.get_center() + np.array([-vector_width*0.18, 0, 0]),  # 0.7
            numerical_vector.get_center() + np.array([0, 0, 0]),                    # 0.9
            numerical_vector.get_center() + np.array([vector_width*0.18, 0, 0]),    # 0.4
            numerical_vector.get_center() + np.array([vector_width*0.36, 0, 0])     # 0.6
        ]
        
        label_positions = [
            [-vector_width*0.5, -2.5, 0],   # Tempo - far left
            [-vector_width*0.25, -3.2, 0],  # Energy - left-center but lower
            [0, -2.8, 0],                   # Danceability - center
            [vector_width*0.25, -3.2, 0],   # Instrumentation - right-center but lower
            [vector_width*0.5, -2.5, 0]     # Vocals - far right
        ]
        
        for i, feature in enumerate(features):
            # Create feature label with clearer font
            feature_label = Text(feature, font_size=28, slant=ITALIC)
            
            # Position labels according to the spread arrangement
            feature_label.move_to(label_positions[i])
            
            # Create blue arrows pointing directly to each numerical value
            number_position = value_positions[i]
            
            # Create straight arrows for all labels (no curved arrows to avoid the circle effect)
            arrow = Arrow(
                start=feature_label.get_top(),
                end=number_position,
                buff=0.1,
                max_tip_length_to_length_ratio=0.15,
                stroke_width=2,
                color=BLUE
            )
            
            feature_labels.add(feature_label)
            arrows.add(arrow)
        
        self.play(Create(feature_labels), Create(arrows))
        self.wait(2)
        
        # Fade out the feature vector and show the music vector space
        self.play(FadeOut(VGroup(vector_title, numerical_vector, feature_labels, arrows)))
        
        # Create the coordinate system - further reduced size to ensure it fits completely
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],  # Reduced y-range
            x_length=8,  # Reduced width
            y_length=5.5,  # Further reduced height to ensure nothing is cut off
            axis_config={"include_tip": True, "include_numbers": True}
        )
        
        # Add grid lines (like graph paper in the example)
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],  # Match axes y-range
            x_length=8,  # Match axes x-length
            y_length=5.5,  # Match axes y-length
            background_line_style={
                "stroke_color": LIGHT_GREY,
                "stroke_width": 0.5,
                "stroke_opacity": 0.5
            }
        )
        
        # Position grid back down as requested
        grid_group = VGroup(grid, axes)
        grid_group.move_to(ORIGIN).shift(DOWN * 0.2)  # Moved down slightly
        
        self.play(Create(grid), Create(axes))
        
        # Create profile vector
        profile_vector = Arrow(axes.coords_to_point(0, 0), axes.coords_to_point(2, 1.5), 
                             buff=0, color=BLUE, stroke_width=6, max_tip_length_to_length_ratio=0.2)
        profile_label = Text("Song Profile", font_size=28, color=BLUE)
        
        # Position label at the end of the arrow with proper alignment
        end_point = profile_vector.get_end()
        profile_label.move_to(end_point + np.array([0.7, 0.4, 0]))
        
        self.play(Create(profile_vector), Write(profile_label))
        self.wait(5)  # Increased pause after profile vector appears
        
        # Create similar song vectors with album art images
        similar_vectors = VGroup()
        similar_images = Group()  # Changed to Group since ImageMobject isn't a VMobject
        similar_check_marks = VGroup()
        
        # Define points and image paths (only 2 pop songs)
        similar_points = [(2.5, 2), (3, 1)]  # Just 2 points for pop songs
        similar_image_paths = [
            "assets/starboy.png",  # Updated file extension to match actual file
            "assets/tameimpala.png"  # Updated file extension to match actual file
        ]
        
        # Create arrows and images for similar songs
        for i, (point, img_path) in enumerate(zip(similar_points, similar_image_paths)):
            # Create vector arrow
            vec = Arrow(
                start=axes.coords_to_point(0, 0),
                end=axes.coords_to_point(*point),
                buff=0, 
                color=GREEN,
                stroke_width=5,
                max_tip_length_to_length_ratio=0.2
            )
            similar_vectors.add(vec)
            
            # Load and position actual image with more precise positioning
            img = ImageMobject(img_path).scale(0.4)  # Adjust scale as needed
            
            # Custom positioning for each image to align better with vector tips
            if i == 0:  # First similar song (starboy)
                img.move_to(vec.get_end() + np.array([0.6, 0.6, 0]))
            else:  # Second similar song (tameimpala)
                img.move_to(vec.get_end() + np.array([0.6, 0.2, 0]))
                
            similar_images.add(img)
            
            # No check marks as requested
            pass  # Skip adding check marks
        
        # Create different song vectors with album art
        different_vectors = VGroup()
        different_images = Group()  # Changed to Group since ImageMobject isn't a VMobject
        different_x_marks = VGroup()
        
        # Define points and image paths for different songs (only 1 Beethoven)
        different_points = [(-2.5, -1.5)]  # Just 1 point for Beethoven
        different_image_paths = [
            "assets/beethoven.jpeg"  # Updated file extension to match actual file
        ]
        
        # Create arrows and images for different songs
        for i, (point, img_path) in enumerate(zip(different_points, different_image_paths)):
            # Create vector arrow
            vec = Arrow(
                start=axes.coords_to_point(0, 0),
                end=axes.coords_to_point(*point),
                buff=0, 
                color=RED,
                stroke_width=5,
                max_tip_length_to_length_ratio=0.2
            )
            different_vectors.add(vec)

            img = ImageMobject(img_path).scale(0.4)  # Adjust scale as needed
            
            # More precise positioning for Beethoven image
            img.move_to(vec.get_end() + np.array([-0.7, -0.2, 0]))
            different_images.add(img)
               
        # Play animations for similar and different songs
        self.play(
            Create(similar_vectors),
            FadeIn(similar_images)
            # No check marks to write
        )
        self.wait(5)  
        
        self.play(
            Create(different_vectors),
            FadeIn(different_images)
        )
        self.wait(10)  
        
        self.play(
            FadeOut(title), 
            FadeOut(grid), 
            FadeOut(axes),
            FadeOut(profile_vector), 
            FadeOut(profile_label),
            FadeOut(similar_vectors),
            FadeOut(different_vectors),
            FadeOut(similar_images),
            FadeOut(different_images)
        )
        
# To render all scenes in sequence, you can run them individually with Manim's CLI:
# For example:
# manim -p -ql cosine_similarity.py CosineSimilarityTitle
# manim -p -ql cosine_similarity.py CosineSimilarityIntuition
# ... and so on for each scene.
