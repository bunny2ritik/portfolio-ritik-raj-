#!/usr/bin/env python3
"""
Generate meaningful cybersecurity project images for the portfolio.
Each image represents the project's theme with professional design.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_image(filename, width, height, bg_color, title, subtitle, accent_color, icon_design_func):
    """Create a project image with given specifications."""
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img, "RGBA")
    
    # Draw accent bar
    bar_height = 8
    draw.rectangle([(0, 0), (width, bar_height)], fill=accent_color)
    
    # Draw icon area
    icon_design_func(draw, width, height, accent_color)
    
    # Draw title and subtitle
    title_y = height - 120
    subtitle_y = height - 60
    
    # Title (white text)
    draw.text((30, title_y), title, fill=(255, 255, 255), font=None)
    # Subtitle (gray text)
    draw.text((30, subtitle_y), subtitle, fill=(180, 180, 180), font=None)
    
    output_path = f"/Users/bunny2ritik/Downloads/rajesh-portfolio/public/images/{filename}"
    img.save(output_path, "PNG")
    print(f"✓ Created: {filename}")

# Color scheme
DARK_BG = (20, 20, 30)
CYAN = (34, 211, 238)
MAGENTA = (236, 72, 153)
RED = (239, 68, 68)
GREEN = (34, 197, 94)
BLUE = (59, 130, 246)
PURPLE = (168, 85, 247)

# Image dimensions
WIDTH, HEIGHT = 600, 400

# 1. DDoS Detection & Mitigation System
def ddos_icon(draw, w, h, color):
    """Draw network attack/shield icon."""
    # Shield outline
    cx, cy = w // 2, h // 2 - 40
    shield_w, shield_h = 120, 140
    draw.rectangle(
        [(cx - shield_w//2, cy - shield_h//2), (cx + shield_w//2, cy + shield_h//2)],
        outline=color, width=3
    )
    # Attack waves
    for i in range(3):
        radius = 80 + (i * 30)
        draw.ellipse(
            [(cx - radius, cy - radius), (cx + radius, cy + radius)],
            outline=RED, width=2
        )
    # Center dot (security)
    draw.ellipse([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill=color)

create_image(
    "ddos_detection.png", WIDTH, HEIGHT, DARK_BG,
    "DDoS Detection & Mitigation",
    "Real-time network security monitoring", RED, ddos_icon
)

# 2. Digital Forensics & Incident Response
def forensics_icon(draw, w, h, color):
    """Draw magnifying glass + data icon."""
    # Magnifying glass
    cx, cy = w // 2 - 30, h // 2 - 40
    draw.ellipse([(cx - 40, cy - 40), (cx + 40, cy + 40)], outline=color, width=3)
    draw.line([(cx + 35, cy + 35), (cx + 60, cy + 60)], fill=color, width=3)
    # Data blocks inside
    draw.rectangle([(cx - 25, cy - 20), (cx - 5, cy)], fill=color, outline=color)
    draw.rectangle([(cx + 5, cy - 20), (cx + 25, cy)], fill=color, outline=color)
    draw.rectangle([(cx - 25, cy + 5), (cx + 25, cy + 25)], outline=color, width=2)

create_image(
    "forensics_tool.png", WIDTH, HEIGHT, DARK_BG,
    "Digital Forensics & IR",
    "Automated evidence collection & analysis", PURPLE, forensics_icon
)

# 3. Mait Android App
def android_icon(draw, w, h, color):
    """Draw Android phone icon."""
    # Phone body
    phone_w, phone_h = 80, 140
    cx, cy = w // 2, h // 2 - 40
    draw.rectangle(
        [(cx - phone_w//2, cy - phone_h//2), (cx + phone_w//2, cy + phone_h//2)],
        outline=color, width=3, fill=(10, 10, 10)
    )
    # Screen
    draw.rectangle(
        [(cx - 30, cy - 50), (cx + 30, cy + 40)],
        fill=(30, 60, 80), outline=CYAN, width=2
    )
    # Home button
    draw.ellipse([(cx - 8, cy + 50), (cx + 8, cy + 66)], outline=color, width=2)

create_image(
    "mait_android.png", WIDTH, HEIGHT, DARK_BG,
    "Mait Android App",
    "Utility app with Lost & Found management", GREEN, android_icon
)

# 4. Network Security Architecture
def network_icon(draw, w, h, color):
    """Draw network nodes/topology icon."""
    cx, cy = w // 2, h // 2 - 40
    # Center node
    draw.ellipse([(cx - 15, cy - 15), (cx + 15, cy + 15)], fill=color)
    # Surrounding nodes
    radius = 60
    for i in range(4):
        angle = (i * 90) * 3.14159 / 180
        import math
        x = int(cx + radius * math.cos(angle))
        y = int(cy + radius * math.sin(angle))
        draw.ellipse([(x - 12, y - 12), (x + 12, y + 12)], outline=color, width=2)
        draw.line([(cx, cy), (x, y)], fill=color, width=2)

create_image(
    "network_design.png", WIDTH, HEIGHT, DARK_BG,
    "Network Security Architecture",
    "Secure VLAN design & TCP/IP optimization", BLUE, network_icon
)

# 5. Wi-Fi Security Demonstration
def wifi_icon(draw, w, h, color):
    """Draw Wi-Fi signal icon."""
    cx, cy = w // 2, h // 2 - 40
    # Wi-Fi arcs
    for i in range(1, 4):
        size = 25 * i
        draw.arc(
            [(cx - size, cy - size), (cx + size, cy + size)],
            0, 180, fill=color, width=3
        )
    # Base dot
    draw.ellipse([(cx - 6, cy + 35), (cx + 6, cy + 47)], fill=color)
    # Security lock
    lock_x, lock_y = cx + 50, cy - 30
    draw.rectangle([(lock_x - 15, lock_y), (lock_x + 15, lock_y + 25)], 
                   outline=RED, width=2, fill=(20, 20, 30))
    draw.ellipse([(lock_x - 12, lock_y - 12), (lock_x + 12, lock_y)], 
                 outline=RED, width=2)

create_image(
    "wifi_security.png", WIDTH, HEIGHT, DARK_BG,
    "Wi-Fi Security Demonstration",
    "Ethical hacking & vulnerability testing", RED, wifi_icon
)

print("\n✅ All project images generated successfully!")
