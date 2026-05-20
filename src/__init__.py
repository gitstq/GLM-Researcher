"""
GLM-Researcher - Local Academic Research Writing Assistant
============================================================

A lightweight, zero-dependency academic research writing assistant CLI tool
powered by Zhipu AI's GLM-5.1 model.

Author: GLM-Researcher Team
License: MIT
Version: 1.0.0
"""

from .glm_researcher import (
    GLMClient,
    AcademicPaperGenerator,
    CitationChecker,
    PaperOutlineGenerator,
    print_banner,
    print_success,
    print_error,
    print_info,
    __version__
)

__all__ = [
    'GLMClient',
    'AcademicPaperGenerator',
    'CitationChecker',
    'PaperOutlineGenerator',
    'print_banner',
    'print_success',
    'print_error',
    'print_info',
    '__version__'
]
