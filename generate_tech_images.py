#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create output directory if it doesn't exist
output_dir = "/Users/bunny2ritik/Downloads/rajesh-portfolio/public/images"
os.makedirs(output_dir, exist_ok=True)

def create_tech_image(filename, name, color, bg_color, design_func):
    """Create a tech stack logo image."""
    img = Image.new('RGBA', (512, 512), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw background with gradient effect
    for y in range(512):
        ratio = y / 512
        r = int(bg_color[0] * (1 - ratio * 0.3))
        g = int(bg_color[1] * (1 - ratio * 0.3))
        b = int(bg_color[2] * (1 - ratio * 0.3))
        draw.line([(0, y), (512, y)], fill=(r, g, b, 255))
    
    # Draw the design
    design_func(draw, color)
    
    # Save as WebP
    webp_path = os.path.join(output_dir, filename)
    img.save(webp_path, 'WEBP', quality=90)
    print(f"✓ Created: {filename}")

def python_logo(draw, color):
    """Python logo design."""
    # Blue and yellow snake-like shape
    draw.ellipse([100, 100, 220, 220], fill=(59, 89, 152, 255), outline=(255, 255, 255, 100), width=3)
    draw.ellipse([280, 250, 400, 370], fill=(255, 200, 50, 255), outline=(255, 255, 255, 100), width=3)
    draw.polygon([(220, 150), (280, 250), (250, 200)], fill=(200, 150, 255, 200))

def kali_linux_logo(draw, color):
    """Kali Linux dragon logo design."""
    # Dragon-like creature in red/black
    draw.ellipse([150, 100, 350, 300], fill=(200, 20, 20, 255), outline=(255, 255, 255, 100), width=3)
    draw.polygon([(256, 120), (300, 200), (256, 280)], fill=(50, 50, 50, 255))
    draw.ellipse([220, 160, 250, 190], fill=(255, 255, 255, 255))

def aws_logo(draw, color):
    """AWS logo design - orange arrow."""
    # Orange arrow pointing up-right
    draw.polygon([(150, 350), (256, 100), (362, 350), (310, 350), (256, 200), (202, 350)], 
                 fill=(255, 150, 0, 255), outline=(255, 255, 255, 100))

def git_logo(draw, color):
    """Git logo design - branching."""
    # Red circles connected with lines (branching)
    draw.ellipse([180, 120, 220, 160], fill=(222, 67, 58, 255), outline=(255, 255, 255, 100), width=3)
    draw.ellipse([140, 280, 180, 320], fill=(222, 67, 58, 255), outline=(255, 255, 255, 100), width=3)
    draw.ellipse([300, 280, 340, 320], fill=(222, 67, 58, 255), outline=(255, 255, 255, 100), width=3)
    draw.line([(200, 160), (160, 280)], fill=(222, 67, 58, 255), width=4)
    draw.line([(200, 160), (320, 280)], fill=(222, 67, 58, 255), width=4)

def java_logo(draw, color):
    """Java logo design - coffee cup."""
    # Coffee cup shape in brown/orange
    draw.rectangle([150, 150, 362, 380], fill=(244, 128, 30, 255), outline=(255, 255, 255, 100), width=3)
    draw.ellipse([150, 140, 362, 200], fill=(244, 128, 30, 255), outline=(255, 255, 255, 100), width=3)
    draw.rectangle([340, 200, 380, 340], fill=(244, 128, 30, 255), outline=(255, 255, 255, 100), width=3)

def kotlin_logo(draw, color):
    """Kotlin logo design - geometric shape."""
    # Purple/pink geometric design
    draw.polygon([(100, 400), (256, 100), (412, 400)], fill=(181, 54, 226, 255), outline=(255, 255, 255, 100))
    draw.polygon([(200, 300), (256, 200), (312, 300)], fill=(100, 20, 150, 255), outline=(255, 255, 255, 100))

def sql_logo(draw, color):
    """SQL logo design - database."""
    # Blue database cylinder
    draw.ellipse([150, 100, 362, 160], fill=(0, 150, 200, 255), outline=(255, 255, 255, 100), width=3)
    draw.rectangle([150, 160, 362, 350], fill=(0, 120, 160, 255), outline=(255, 255, 255, 100), width=3)
    draw.ellipse([150, 330, 362, 390], fill=(0, 100, 140, 255), outline=(255, 255, 255, 100), width=3)
    draw.line([(150, 200), (362, 200)], fill=(0, 180, 220, 255), width=2)
    draw.line([(150, 270), (362, 270)], fill=(0, 180, 220, 255), width=2)

def wireshark_logo(draw, color):
    """Wireshark logo design - network waves."""
    # Blue waves representing network capture
    draw.ellipse([100, 150, 412, 450], fill=None, outline=(0, 128, 215, 255), width=8)
    draw.ellipse([140, 190, 372, 410], fill=None, outline=(0, 160, 255, 255), width=6)
    draw.ellipse([180, 230, 332, 370], fill=None, outline=(100, 200, 255, 255), width=4)
    draw.ellipse([220, 250, 292, 350], fill=(0, 128, 215, 255))

def nodejs_logo(draw, color):
    """Node.js logo design - green leaf."""
    # Green leaf/node shape
    draw.ellipse([150, 100, 362, 300], fill=(104, 204, 86, 255), outline=(255, 255, 255, 100), width=3)
    draw.ellipse([180, 200, 332, 380], fill=(68, 175, 60, 255), outline=(255, 255, 255, 100), width=3)
    draw.polygon([(256, 100), (180, 140), (332, 140)], fill=(104, 204, 86, 255))

# Generate all tech images
create_tech_image("python.webp", "Python", (59, 89, 152), (10, 10, 30, 255), python_logo)
create_tech_image("kali-linux.webp", "Kali Linux", (200, 20, 20), (10, 10, 30, 255), kali_linux_logo)
create_tech_image("aws.webp", "AWS", (255, 150, 0), (10, 10, 30, 255), aws_logo)
create_tech_image("git.webp", "Git", (222, 67, 58), (10, 10, 30, 255), git_logo)
create_tech_image("java.webp", "Java", (244, 128, 30), (10, 10, 30, 255), java_logo)
create_tech_image("kotlin.webp", "Kotlin", (181, 54, 226), (10, 10, 30, 255), kotlin_logo)
create_tech_image("sql.webp", "SQL", (0, 150, 200), (10, 10, 30, 255), sql_logo)
create_tech_image("wireshark.webp", "Wireshark", (0, 128, 215), (10, 10, 30, 255), wireshark_logo)
create_tech_image("node2.webp", "Node.js", (104, 204, 86), (10, 10, 30, 255), nodejs_logo)

print("\n✅ All tech stack images generated successfully!")
