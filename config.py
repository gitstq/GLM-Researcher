#!/usr/bin/env python3
"""
Configuration file for GLM-Researcher
Store your API key and preferences here
"""

# Zhipu AI API Key
# Get your key from: https://open.bigmodel.cn/
ZHIPU_API_KEY = ""  # Set your API key here

# Default model (glm-4-flash is cost-effective, glm-4 for higher quality)
DEFAULT_MODEL = "glm-4-flash"

# Temperature setting (0.0-1.0, lower = more focused, higher = more creative)
DEFAULT_TEMPERATURE = 0.7

# Maximum tokens for responses
DEFAULT_MAX_TOKENS = 2048

# Output directory
DEFAULT_OUTPUT_DIR = "."

# Available models
AVAILABLE_MODELS = {
    "glm-4-flash": "Fast and cost-effective for most tasks",
    "glm-4": "Higher quality, slightly slower",
    "glm-4-plus": "Best quality, higher cost",
    "glm-4-airx": "Optimized for academic writing"
}

# Paper templates
PAPER_TEMPLATES = {
    "empirical": "Empirical Research Paper",
    "theoretical": "Theoretical/Conceptual Paper",
    "review": "Literature Review Paper"
}

# Writing styles
WRITING_STYLES = {
    "academic": "Formal academic style with precise language",
    "formal": "Professional formal style",
    "simple": "Clear and accessible style"
}
