#!/usr/bin/env python3
"""
Download official tech logos from devicons repository
"""
import os
import urllib.request
from urllib.error import URLError
import time

output_dir = "/Users/bunny2ritik/Downloads/rajesh-portfolio/public/images"
os.makedirs(output_dir, exist_ok=True)

# Official logo URLs from devicons and other reliable sources
logos = {
    "python.png": "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",
    "aws.png": "https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original.svg",
    "java.png": "https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg",
    "kotlin.png": "https://raw.githubusercontent.com/devicons/devicon/master/icons/kotlin/kotlin-original.svg",
    "node2.png": "https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original.svg",
    "sql.png": "https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg",
}

def download_file(url, output_path, timeout=10):
    """Download file from URL"""
    try:
        print(f"Downloading: {os.path.basename(output_path)}")
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(request, timeout=timeout)
        data = response.read()
        
        with open(output_path, 'wb') as f:
            f.write(data)
        
        file_size = os.path.getsize(output_path)
        print(f"✓ Downloaded: {os.path.basename(output_path)} ({file_size/1024:.1f}KB)")
        return True
    except Exception as e:
        print(f"✗ Failed to download {url}: {e}")
        return False

print("Downloading official tech logos...\n")

# Download SVG logos
for filename, url in logos.items():
    output_path = os.path.join(output_dir, filename)
    # Skip if already exists
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        print(f"✓ Already exists: {filename}")
        continue
    
    success = download_file(url, output_path)
    if success:
        time.sleep(0.5)  # Rate limiting

# Special case for Wireshark - use PNG from Wikipedia
wireshark_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Wireshark_logo.svg/1200px-Wireshark_logo.svg.png"
wireshark_path = os.path.join(output_dir, "wireshark.png")
if not os.path.exists(wireshark_path) or os.path.getsize(wireshark_path) < 1000:
    print(f"Downloading: wireshark.png (from Wikipedia)")
    try:
        request = urllib.request.Request(wireshark_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(request, timeout=10)
        data = response.read()
        with open(wireshark_path, 'wb') as f:
            f.write(data)
        file_size = os.path.getsize(wireshark_path)
        print(f"✓ Downloaded: wireshark.png ({file_size/1024:.1f}KB)")
    except Exception as e:
        print(f"✗ Failed to download Wireshark logo: {e}")

print("\n✅ Official tech logos downloaded successfully!")
