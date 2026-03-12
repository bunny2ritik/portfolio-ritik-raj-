#!/usr/bin/env python3
from PIL import Image, ImageDraw
import os

# Create output directory if it doesn't exist
output_dir = "/Users/bunny2ritik/Downloads/rajesh-portfolio/public/images"
os.makedirs(output_dir, exist_ok=True)

def create_tech_logo(filename, design_func):
    """Create a high-contrast tech stack logo image with white background."""
    # Create with white background for better contrast
    img = Image.new('RGB', (512, 512), (240, 240, 240))
    draw = ImageDraw.Draw(img)
    
    # Draw the design
    design_func(draw)
    
    # Save as PNG
    png_path = os.path.join(output_dir, filename)
    img.save(png_path, 'PNG')
    print(f"✓ Created: {filename}")

def python_logo(draw):
    """Python official logo colors: blue and yellow."""
    # Large circle background with gradient effect
    draw.ellipse([40, 40, 472, 472], outline=(55, 118, 185, 255), width=0)
    
    # Python snake shape - MUCH LARGER
    # Top circle (head) - blue
    draw.ellipse([100, 60, 280, 240], fill=(55, 118, 185, 255), outline=(0, 50, 150, 255), width=4)
    # Bottom circle (body) - yellow
    draw.ellipse([270, 260, 450, 440], fill=(255, 189, 68, 255), outline=(200, 140, 0, 255), width=4)
    # Connection line
    draw.line([(190, 240), (360, 260)], fill=(100, 100, 200, 255), width=25)
    # Eyes - white
    draw.ellipse([130, 100, 170, 140], fill=(255, 255, 255, 255))
    draw.ellipse([210, 100, 250, 140], fill=(255, 255, 255, 255))
    # Pupils
    draw.ellipse([140, 110, 160, 130], fill=(0, 0, 0, 255))
    draw.ellipse([220, 110, 240, 130], fill=(0, 0, 0, 255))

def kali_linux_logo(draw):
    """Kali Linux - dragon style in red/black - HIGH CONTRAST."""
    # Vertical line through center
    draw.line([(256, 80), (256, 432)], fill=(220, 20, 20, 255), width=16)
    
    # Dragon shapes on left (red) and right (black)
    # Left side - Red
    draw.ellipse([80, 120, 240, 280], fill=(220, 20, 20, 255), outline=(100, 0, 0, 255), width=3)
    draw.polygon([(160, 120), (140, 80), (180, 80)], fill=(220, 20, 20, 255))
    
    # Right side - Black
    draw.ellipse([272, 120, 432, 280], fill=(0, 0, 0, 255), outline=(100, 100, 100, 255), width=3)
    draw.polygon([(352, 120), (332, 80), (372, 80)], fill=(0, 0, 0, 255))
    
    # Bottom tail
    draw.ellipse([180, 300, 332, 420], fill=(220, 20, 20, 255), outline=(100, 0, 0, 255), width=3)

def aws_logo(draw):
    """AWS - orange arrow pointing up - HIGH CONTRAST."""
    # Large arrow
    draw.polygon([(256, 80), (150, 350), (200, 350), (256, 220), (312, 350), (362, 350)], 
                 fill=(255, 153, 0, 255), outline=(200, 100, 0, 255), width=3)
    # Highlight
    draw.polygon([(256, 120), (200, 280), (256, 200), (312, 280)], 
                 fill=(255, 189, 68, 255), outline=None)

def git_logo(draw):
    """Git - red branching diagram - LARGE."""
    # Three nodes
    draw.ellipse([180, 80, 280, 180], fill=(222, 67, 58, 255), outline=(100, 0, 0, 255), width=4)  # top
    draw.ellipse([80, 300, 180, 400], fill=(222, 67, 58, 255), outline=(100, 0, 0, 255), width=4)  # left
    draw.ellipse([332, 300, 432, 400], fill=(222, 67, 58, 255), outline=(100, 0, 0, 255), width=4)  # right
    
    # Branch lines
    draw.line([(230, 180), (130, 300)], fill=(222, 67, 58, 255), width=12)
    draw.line([(230, 180), (382, 300)], fill=(222, 67, 58, 255), width=12)

def java_logo(draw):
    """Java - coffee cup - HIGH CONTRAST."""
    # Cup body
    draw.rectangle([130, 180, 340, 380], fill=(244, 128, 30, 255), outline=(150, 60, 0, 255), width=4)
    # Cup rim
    draw.ellipse([130, 170, 340, 210], fill=(244, 128, 30, 255), outline=(150, 60, 0, 255), width=4)
    # Cup handle
    draw.arc([(340, 190), (420, 370)], 0, 180, fill=(244, 128, 30, 255), width=14)
    # Steam wisps
    draw.line([(150, 160), (130, 80)], fill=(180, 120, 80, 255), width=12)
    draw.line([(256, 160), (250, 60)], fill=(180, 120, 80, 255), width=12)
    draw.line([(360, 160), (380, 80)], fill=(180, 120, 80, 255), width=12)

def kotlin_logo(draw):
    """Kotlin - purple mountain - HIGH CONTRAST."""
    # Large triangle
    draw.polygon([(80, 420), (256, 80), (432, 420)], fill=(181, 54, 226, 255), outline=(100, 0, 150, 255), width=4)
    # Inner triangle
    draw.polygon([(160, 320), (256, 160), (352, 320)], fill=(240, 200, 255, 255), outline=(150, 100, 200, 255), width=3)

def sql_logo(draw):
    """SQL - blue database cylinder - HIGH CONTRAST."""
    # Database cylinder top
    draw.ellipse([120, 100, 392, 180], fill=(0, 150, 200, 255), outline=(0, 80, 120, 255), width=3)
    # Database cylinder sides
    draw.rectangle([120, 180, 392, 340], fill=(0, 120, 160, 255), outline=(0, 80, 120, 255), width=3)
    # Database cylinder bottom
    draw.ellipse([120, 320, 392, 400], fill=(0, 100, 140, 255), outline=(0, 80, 120, 255), width=3)
    # Database rings (lines showing layers)
    draw.line([(120, 220), (392, 220)], fill=(0, 200, 255, 255), width=5)
    draw.line([(120, 260), (392, 260)], fill=(0, 200, 255, 255), width=5)
    draw.line([(120, 300), (392, 300)], fill=(0, 200, 255, 255), width=5)

def wireshark_logo(draw):
    """Wireshark - blue network waves - HIGH CONTRAST."""
    # Center dot
    draw.ellipse([240, 240, 272, 272], fill=(0, 200, 255, 255), outline=(0, 80, 150, 255), width=2)
    
    # Concentric circles (network waves) - LARGER and THICKER
    draw.ellipse([100, 100, 412, 412], fill=None, outline=(0, 180, 255, 255), width=16)
    draw.ellipse([140, 140, 372, 372], fill=None, outline=(0, 150, 220, 255), width=12)
    draw.ellipse([180, 180, 332, 332], fill=None, outline=(0, 120, 200, 255), width=8)
    
    # Radar lines
    draw.line([(256, 100), (256, 412)], fill=(0, 200, 255, 255), width=4)
    draw.line([(100, 256), (412, 256)], fill=(0, 200, 255, 255), width=4)

def nodejs_logo(draw):
    """Node.js - green leaf - HIGH CONTRAST."""
    # Main leaf shape
    draw.ellipse([100, 80, 300, 320], fill=(104, 204, 86, 255), outline=(30, 120, 40, 255), width=4)
    draw.ellipse([260, 120, 400, 360], fill=(68, 175, 60, 255), outline=(30, 120, 40, 255), width=4)
    # Leaf stem
    draw.line([(180, 320), (200, 420)], fill=(104, 204, 86, 255), width=16)
    # Leaf vein
    draw.line([(200, 120), (240, 280)], fill=(150, 230, 150, 200), width=5)

# Generate all tech logos with high contrast
create_tech_logo("python.png", python_logo)
create_tech_logo("kali-linux.png", kali_linux_logo)
create_tech_logo("aws.png", aws_logo)
create_tech_logo("git.png", git_logo)
create_tech_logo("java.png", java_logo)
create_tech_logo("kotlin.png", kotlin_logo)
create_tech_logo("node2.png", nodejs_logo)
create_tech_logo("sql.png", sql_logo)
create_tech_logo("wireshark.png", wireshark_logo)

print("\n✅ All tech logos regenerated with high contrast!")

def kali_linux_logo(draw):
    """Kali Linux - dragon style in red/black - HIGH CONTRAST."""
    # Vertical line through center
    draw.line([(256, 80), (256, 432)], fill=(220, 20, 20, 255), width=16)
    
    # Dragon shapes on left (red) and right (black)
    # Left side - Red
    draw.ellipse([80, 120, 240, 280], fill=(220, 20, 20, 255), outline=(100, 0, 0, 255), width=3)
    draw.polygon([(160, 120), (140, 80), (180, 80)], fill=(220, 20, 20, 255))
    
    # Right side - Black
    draw.ellipse([272, 120, 432, 280], fill=(0, 0, 0, 255), outline=(100, 100, 100, 255), width=3)
    draw.polygon([(352, 120), (332, 80), (372, 80)], fill=(0, 0, 0, 255))
    
    # Bottom tail
    draw.ellipse([180, 300, 332, 420], fill=(220, 20, 20, 255), outline=(100, 0, 0, 255), width=3)

def aws_logo(draw):
    """AWS - orange arrow pointing up."""
    # Circle background
    draw.ellipse([20, 20, 492, 492], fill=(255, 150, 0, 30), outline=(255, 150, 0, 150), width=3)
def aws_logo(draw):
    """AWS - orange arrow pointing up - HIGH CONTRAST."""
    # Large arrow
    draw.polygon([(256, 80), (150, 350), (200, 350), (256, 220), (312, 350), (362, 350)], 
                 fill=(255, 153, 0, 255), outline=(200, 100, 0, 255), width=3)
    # Highlight
    draw.polygon([(256, 120), (200, 280), (256, 200), (312, 280)], 
                 fill=(255, 189, 68, 255), outline=None)

def git_logo(draw):
    """Git - red branching diagram - LARGE."""
    # Three nodes
    draw.ellipse([180, 80, 280, 180], fill=(222, 67, 58, 255), outline=(100, 0, 0, 255), width=4)  # top
    draw.ellipse([80, 300, 180, 400], fill=(222, 67, 58, 255), outline=(100, 0, 0, 255), width=4)  # left
    draw.ellipse([332, 300, 432, 400], fill=(222, 67, 58, 255), outline=(100, 0, 0, 255), width=4)  # right
    
    # Branch lines
    draw.line([(230, 180), (130, 300)], fill=(222, 67, 58, 255), width=12)
    draw.line([(230, 180), (382, 300)], fill=(222, 67, 58, 255), width=12)

def java_logo(draw):
    """Java - coffee cup - HIGH CONTRAST."""
    # Cup body
    draw.rectangle([130, 180, 340, 380], fill=(244, 128, 30, 255), outline=(150, 60, 0, 255), width=4)
    # Cup rim
    draw.ellipse([130, 170, 340, 210], fill=(244, 128, 30, 255), outline=(150, 60, 0, 255), width=4)
    # Cup handle
    draw.arc([(340, 190), (420, 370)], 0, 180, fill=(244, 128, 30, 255), width=14)
    # Steam wisps
    draw.line([(150, 160), (130, 80)], fill=(180, 120, 80, 255), width=12)
    draw.line([(256, 160), (250, 60)], fill=(180, 120, 80, 255), width=12)
    draw.line([(360, 160), (380, 80)], fill=(180, 120, 80, 255), width=12)

def kotlin_logo(draw):
    """Kotlin - purple mountain - HIGH CONTRAST."""
    # Large triangle
    draw.polygon([(80, 420), (256, 80), (432, 420)], fill=(181, 54, 226, 255), outline=(100, 0, 150, 255), width=4)
    # Inner triangle
    draw.polygon([(160, 320), (256, 160), (352, 320)], fill=(240, 200, 255, 255), outline=(150, 100, 200, 255), width=3)

def sql_logo(draw):
    """SQL - blue database cylinder - HIGH CONTRAST."""
    # Database cylinder top
    draw.ellipse([120, 100, 392, 180], fill=(0, 150, 200, 255), outline=(0, 80, 120, 255), width=3)
    # Database cylinder sides
    draw.rectangle([120, 180, 392, 340], fill=(0, 120, 160, 255), outline=(0, 80, 120, 255), width=3)
    # Database cylinder bottom
    draw.ellipse([120, 320, 392, 400], fill=(0, 100, 140, 255), outline=(0, 80, 120, 255), width=3)
    # Database rings (lines showing layers)
    draw.line([(120, 220), (392, 220)], fill=(0, 200, 255, 255), width=5)
    draw.line([(120, 260), (392, 260)], fill=(0, 200, 255, 255), width=5)
    draw.line([(120, 300), (392, 300)], fill=(0, 200, 255, 255), width=5)

def wireshark_logo(draw):
    """Wireshark - blue network waves - HIGH CONTRAST."""
    # Center dot
    draw.ellipse([240, 240, 272, 272], fill=(0, 200, 255, 255), outline=(0, 80, 150, 255), width=2)
    
    # Concentric circles (network waves) - LARGER and THICKER
    draw.ellipse([100, 100, 412, 412], fill=None, outline=(0, 180, 255, 255), width=16)
    draw.ellipse([140, 140, 372, 372], fill=None, outline=(0, 150, 220, 255), width=12)
    draw.ellipse([180, 180, 332, 332], fill=None, outline=(0, 120, 200, 255), width=8)
    
    # Radar lines
    draw.line([(256, 100), (256, 412)], fill=(0, 200, 255, 255), width=4)
    draw.line([(100, 256), (412, 256)], fill=(0, 200, 255, 255), width=4)

def nodejs_logo(draw):
    """Node.js - green leaf - HIGH CONTRAST."""
    # Main leaf shape
    draw.ellipse([100, 80, 300, 320], fill=(104, 204, 86, 255), outline=(30, 120, 40, 255), width=4)
    draw.ellipse([260, 120, 400, 360], fill=(68, 175, 60, 255), outline=(30, 120, 40, 255), width=4)
    # Leaf stem
    draw.line([(180, 320), (200, 420)], fill=(104, 204, 86, 255), width=16)
    # Leaf vein
    draw.line([(200, 120), (240, 280)], fill=(150, 230, 150, 200), width=5)

# Generate all tech logos with high contrast
create_tech_logo("python.png", python_logo)
create_tech_logo("kali-linux.png", kali_linux_logo)
create_tech_logo("aws.png", aws_logo)
create_tech_logo("git.png", git_logo)
create_tech_logo("java.png", java_logo)
create_tech_logo("kotlin.png", kotlin_logo)
create_tech_logo("node2.png", nodejs_logo)
create_tech_logo("sql.png", sql_logo)
create_tech_logo("wireshark.png", wireshark_logo)

print("\n✅ All tech logos regenerated with high contrast!")
