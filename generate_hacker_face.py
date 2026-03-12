#!/usr/bin/env python3
"""
Generate a professional hacker/anonymous face for the 3D character.
Creates a stylized mask with glowing cyan eyes, digital patterns, and cybersecurity aesthetics.
"""

from PIL import Image, ImageDraw
import math

# Image dimensions (should match typical face texture size)
WIDTH, HEIGHT = 1024, 1024
# Colors
BLACK = (11, 11, 11)
DARK_GRAY = (30, 30, 30)
DARK_CYAN = (34, 211, 238)  # #22d3ee - matches site theme
BRIGHT_CYAN = (52, 235, 255)  # Bright cyan for glowing
WHITE = (255, 255, 255)

# Create base image
img = Image.new("RGB", (WIDTH, HEIGHT), BLACK)
draw = ImageDraw.Draw(img, "RGBA")

# 1. Draw base face shape (oval mask)
face_left = WIDTH * 0.2
face_top = HEIGHT * 0.15
face_right = WIDTH * 0.8
face_bottom = HEIGHT * 0.85
draw.ellipse(
    [face_left, face_top, face_right, face_bottom],
    fill=DARK_GRAY,
    outline=DARK_CYAN,
)

# 2. Draw digital grid overlay (cyberpunk feel)
grid_size = 40
for x in range(0, WIDTH, grid_size):
    draw.line([(x, 0), (x, HEIGHT)], fill=(50, 50, 50), width=1)
for y in range(0, HEIGHT, grid_size):
    draw.line([(0, y), (WIDTH, y)], fill=(50, 50, 50), width=1)

# 3. Draw left eye (glowing)
left_eye_x = WIDTH * 0.35
left_eye_y = HEIGHT * 0.4
eye_radius = 45

# Outer glow (bright cyan, transparent)
for r in range(80, 0, -5):
    alpha = int(100 * (1 - r / 80))
    draw.ellipse(
        [
            left_eye_x - r,
            left_eye_y - r,
            left_eye_x + r,
            left_eye_y + r,
        ],
        fill=(*DARK_CYAN, alpha),
    )

# Eye sclera (dark)
draw.ellipse(
    [
        left_eye_x - eye_radius,
        left_eye_y - eye_radius,
        left_eye_x + eye_radius,
        left_eye_y + eye_radius,
    ],
    fill=(5, 5, 5),
    outline=DARK_CYAN,
)

# Iris (cyan)
iris_radius = 25
draw.ellipse(
    [
        left_eye_x - iris_radius,
        left_eye_y - iris_radius,
        left_eye_x + iris_radius,
        left_eye_y + iris_radius,
    ],
    fill=BRIGHT_CYAN,
)

# Pupil (black center)
pupil_radius = 12
draw.ellipse(
    [
        left_eye_x - pupil_radius,
        left_eye_y - pupil_radius,
        left_eye_x + pupil_radius,
        left_eye_y + pupil_radius,
    ],
    fill=(0, 0, 0),
)

# Pupil highlight (bright glow)
highlight_r = 5
draw.ellipse(
    [
        left_eye_x - highlight_r + 8,
        left_eye_y - highlight_r - 8,
        left_eye_x + highlight_r + 8,
        left_eye_y + highlight_r - 8,
    ],
    fill=WHITE,
)

# 4. Draw right eye (same as left)
right_eye_x = WIDTH * 0.65
right_eye_y = HEIGHT * 0.4

# Outer glow
for r in range(80, 0, -5):
    alpha = int(100 * (1 - r / 80))
    draw.ellipse(
        [
            right_eye_x - r,
            right_eye_y - r,
            right_eye_x + r,
            right_eye_y + r,
        ],
        fill=(*DARK_CYAN, alpha),
    )

# Eye sclera
draw.ellipse(
    [
        right_eye_x - eye_radius,
        right_eye_y - eye_radius,
        right_eye_x + eye_radius,
        right_eye_y + eye_radius,
    ],
    fill=(5, 5, 5),
    outline=DARK_CYAN,
)

# Iris
draw.ellipse(
    [
        right_eye_x - iris_radius,
        right_eye_y - iris_radius,
        right_eye_x + iris_radius,
        right_eye_y + iris_radius,
    ],
    fill=BRIGHT_CYAN,
)

# Pupil
draw.ellipse(
    [
        right_eye_x - pupil_radius,
        right_eye_y - pupil_radius,
        right_eye_x + pupil_radius,
        right_eye_y + pupil_radius,
    ],
    fill=(0, 0, 0),
)

# Pupil highlight
draw.ellipse(
    [
        right_eye_x - highlight_r + 8,
        right_eye_y - highlight_r - 8,
        right_eye_x + highlight_r + 8,
        right_eye_y + highlight_r - 8,
    ],
    fill=WHITE,
)

# 5. Draw mouth line (simple slash)
mouth_y = HEIGHT * 0.65
draw.line(
    [(WIDTH * 0.35, mouth_y), (WIDTH * 0.65, mouth_y)],
    fill=DARK_CYAN,
    width=3,
)

# 6. Add scan lines (CRT/digital effect)
for y in range(0, HEIGHT, 4):
    draw.rectangle(
        [(0, y), (WIDTH, y + 2)],
        fill=(0, 0, 0, 30),
    )

# 7. Add subtle circuit lines
def draw_circuit_line(x1, y1, x2, y2):
    segments = 10
    points = []
    for i in range(segments + 1):
        t = i / segments
        x = int(x1 + (x2 - x1) * t)
        y = int(y1 + (y2 - y1) * t)
        points.append((x, y))
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=(50, 100, 100), width=2)

draw_circuit_line(WIDTH * 0.2, HEIGHT * 0.5, WIDTH * 0.3, HEIGHT * 0.3)
draw_circuit_line(WIDTH * 0.8, HEIGHT * 0.5, WIDTH * 0.7, HEIGHT * 0.3)
draw_circuit_line(WIDTH * 0.35, HEIGHT * 0.75, WIDTH * 0.5, HEIGHT * 0.85)
draw_circuit_line(WIDTH * 0.65, HEIGHT * 0.75, WIDTH * 0.5, HEIGHT * 0.85)

# Save image
output_path = "/Users/bunny2ritik/Downloads/rajesh-portfolio/public/images/hacker_face.png"
img.save(output_path, "PNG")
print(f"✓ Hacker face image generated: {output_path}")
print(f"  Image size: {WIDTH}x{HEIGHT}")
print("  Features: Glowing cyan eyes, digital grid, cyberpunk aesthetic")
