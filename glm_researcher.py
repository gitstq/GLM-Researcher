#!/usr/bin/env python3
"""
GLM-Researcher CLI Launcher
Zero-dependency academic research assistant powered by GLM-5.1
"""

import sys
import os
from pathlib import Path

# Add src directory to path
src_dir = Path(__file__).parent / "src"
sys.path.insert(0, str(src_dir))

# Import and run main
from glm_researcher import main

if __name__ == "__main__":
    main()
