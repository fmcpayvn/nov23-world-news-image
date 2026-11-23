#!/usr/bin/env python3
"""Regenerate the 23 November 2026 world-news front page (entry.png).

Run: python3 main.py
Reads stories.json and draws entry.png (1024x1024) with render.py.
"""
import subprocess
import sys

if __name__ == "__main__":
    subprocess.run([sys.executable, "render.py"], check=True)
    print("entry.png regenerated.")
