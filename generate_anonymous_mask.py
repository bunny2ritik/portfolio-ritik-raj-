#!/usr/bin/env python3
"""
Generate an iconic Guy Fawkes/Anonymous mask face for the 3D character.
Creates the classic white mask with black eye holes and red cheeks.
"""

from PIL import Image, ImageDraw
import math

# Image dimensions
WIDTH, HEIGHT = 1024, 1024

# Colors
BLACK = (0, 0, 0)
WHITE = (245, 245, 245)
RED = (220, 20, 60)  # Crimson red for cheeks
DARK_RED = (139, 0, 0)  # Dark red for shading
GRAY = (200, 200, 200)

# Create base image with dark background
img = Image.new("RGB", (WIDTH, HEIGHT), (30, 30, 30))
draw = ImageDraw.Draw(img, "RGBA")

# 1. Draw main white mask face (oval shape)
face_left = WIDTH * 0.2
face_top = HEIGHT * 0.15
face_right = WIDTH * 0.8
face_bottom = HEIGHT * 0.85
draw.ellipse(
    [face_left, face_top, face_right, face_bottom],
    fill=WHITE,
    outline=GRAY,
)

# 2. Draw left cheek (red circle for iconic character)
left_cheek_x = WIDTH * 0.3
left_cheek_y = HEIGHT * 0.55
cheek_radius = 60
draw.ellipse(
    [
        left_cheek_x - cheek_radius,
        left_cheek_y - cheek_radius,
        left_cheek_x + cheek_radius,
        left_cheek_y + cheek_radius,
    ],
    fill=RED,
)
# Shading on cheek
draw.ellipse(
    [
        left_cheek_x - cheek_radius + 15,
        left_cheek_y - cheek_radius + 15,
        left_cheek_x + cheek_radius - 15,
        left_cheek_y + cheek_radius - 15,
    ],
    fill=(200, 50, 80),
)

# 3. Draw right cheek (red circle)
right_cheek_x = WIDTH * 0.7
right_cheek_y = HEIGHT * 0.55
draw.ellipse(
    [
        right_cheek_x - cheek_radius,
        right_cheek_y - cheek_radius,
        right_cheek_x + cheek_radius,
        right_cheek_y + cheek_radius,
    ],
    fill=RED,
)
# Shading on cheek
draw.ellipse(
    [
        right_cheek_x - cheek_radius + 15,
        right_cheek_y - cheek_radius + 15,
        right_cheek_x + cheek_radius - 15,
        right_cheek_y + cheek_radius - 15,
    ],
    fill=(200, 50, 80),
)

# 4. Draw left eye (black oval hole)
left_eye_x = WIDTH * 0.35
left_eye_y = HEIGHT * 0.35
eye_width = 50
eye_height = 65
draw.ellipse(
    [
        left_eye_x - eye_width,
        left_eye_y - eye_height,
        left_eye_x + eye_width,
        left_eye_y + eye_height,
    ],
    fill=BLACK,
)

# 5. Draw right eye (black oval hole)
right_eye_x = WIDTH * 0.65
right_eye_y = HEIGHT * 0.35
draw.ellipse(
    [
        right_eye_x - eye_width,
        right_eye_y - eye_height,
        right_eye_x + eye_width,
        right_eye_y + eye_height,
    ],
    fill=BLACK,
)

# 6. Draw mouth (horizontal line with slight smile)
mouth_y = HEIGHT * 0.65
draw.line(
    [(WIDTH * 0.35, mouth_y), (WIDTH * 0.65, mouth_y)],
    fill=BLACK,
    width=5,
)
# Smile corners (upturned)
draw.line([(WIDTH * 0.35, mouth_y), (WIDTH * 0.3, mouth_y + 15)], fill=BLACK, width=4)
draw.line([(WIDTH * 0.65, mouth_y), (WIDTH * 0.7, mouth_y + 15)], fill=BLACK, width=4)

# 7. Add nose line (vertical)
nose_x = WIDTH * 0.5
draw.line(
    [(nose_x, HEIGHT * 0.3), (nose_x, HEIGHT * 0.65)],
    fill=BLACK,
    width=3,
)

# 8. Add forehead detail lines (wrinkles/character)
draw.line(
    [(WIDTH * 0.3, HEIGHT * 0.2), (WIDTH * 0.7, HEIGHT * 0.2)],
    fill=GRAY,
    width=2,
)
draw.line(
    [(WIDTH * 0.3, HEIGHT * 0.25), (WIDTH * 0.7, HEIGHT * 0.25)],
    fill=GRAY,
    width=1,
)

# 9. Add eyebrow lines for more character
draw.line(
    [(WIDTH * 0.25, HEIGHT * 0.28), (WIDTH * 0.45, HEIGHT * 0.25)],
    fill=BLACK,
    width=2,
)
draw.line(
    [(WIDTH * 0.55, HEIGHT * 0.25), (WIDTH * 0.75, HEIGHT * 0.28)],
    fill=BLACK,
    width=2,
)

# 10. Add subtle shading on mask edges (3D effect)
for i in range(1, 15):
    alpha = int(30 * (i / 15))
    shade = 200 - alpha
    draw.ellipse(
        [
            face_left - i,
            face_top - i,
            face_right + i,
            face_bottom + i,
        ],
        outline=(shade, shade, shade),
        width=1,
    )

# Save image
output_path = "/Users/bunny2ritik/Downloads/rajesh-portfolio/public/images/hacker_face.png"
img.save(output_path, "PNG")
print(f"✓ Anonymous mask face generated: {output_path}")
print(f"  Image size: {WIDTH}x{HEIGHT}")
print("  Features: Classic Guy Fawkes/Anonymous white mask with red cheeks, black eyes and smile")
