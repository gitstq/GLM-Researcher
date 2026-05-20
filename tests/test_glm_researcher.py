#!/usr/bin/env python3
"""
Unit Tests for GLM-Researcher
Run with: python3 -m pytest tests/ -v
"""

import unittest
import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

try:
    from glm_researcher import (
        CitationChecker, PaperOutlineGenerator, save_to_file,
        Colors, colorize, print_banner
    )
except ImportError as e:
    print(f"Warning: Could not import all modules: {e}")


class TestCitationChecker(unittest.TestCase):
    """Test citation extraction and formatting."""
    
    def setUp(self):
        self.checker = CitationChecker()
    
    def test_extract_parenthetical_citations(self):
        """Test extraction of parenthetical citations."""
        text = "Previous research (Smith, 2020) shows that (Jones et al., 2019, p. 45) demonstrates"
        citations = self.checker.extract_citations(text)
        self.assertTrue(len(citations) >= 2)
    
    def test_extract_numeric_citations(self):
        """Test extraction of numeric citations."""
        text = "This approach [1] has been improved [2, 3, 4]"
        citations = self.checker.extract_citations(text)
        self.assertTrue(len(citations) >= 2)
    
    def test_validate_citation(self):
        """Test citation validation."""
        valid = self.checker.validate_citation_format("Smith, 2020")
        self.assertTrue(valid["valid"])
        
        invalid = self.checker.validate_citation_format("Some text without citation")
        self.assertFalse(invalid["valid"])
    
    def test_format_apa(self):
        """Test APA formatting."""
        ref = self.checker.format_apa(
            author="Smith, J.",
            year="2020",
            title="Understanding AI",
            source="Journal of AI",
            doi="10.1234/example",
            pages="45-67"
        )
        self.assertIn("Smith, J.", ref)
        self.assertIn("2020", ref)
        self.assertIn("Understanding AI", ref)


class TestPaperOutlineGenerator(unittest.TestCase):
    """Test paper outline generation."""
    
    def test_get_empirical_template(self):
        """Test empirical research template."""
        template = PaperOutlineGenerator.get_template("empirical")
        self.assertEqual(template["name"], "Empirical Research Paper")
        self.assertIn("Abstract", "\n".join(template["sections"]))
        self.assertIn("Methodology", "\n".join(template["sections"]))
    
    def test_get_theoretical_template(self):
        """Test theoretical paper template."""
        template = PaperOutlineGenerator.get_template("theoretical")
        self.assertEqual(template["name"], "Theoretical/Conceptual Paper")
    
    def test_get_review_template(self):
        """Test literature review template."""
        template = PaperOutlineGenerator.get_template("review")
        self.assertEqual(template["name"], "Literature Review Paper")
    
    def test_list_templates(self):
        """Test listing all templates."""
        templates = PaperOutlineGenerator.list_templates()
        self.assertIn("empirical", templates)
        self.assertIn("theoretical", templates)
        self.assertIn("review", templates)


class TestFileOperations(unittest.TestCase):
    """Test file save operations."""
    
    def test_save_to_file(self):
        """Test saving content to file."""
        import tempfile
        
        with tempfile.TemporaryDirectory() as tmpdir:
            content = "Test content"
            filename = save_to_file(content, "test.txt", tmpdir)
            
            self.assertTrue(os.path.exists(filename))
            
            with open(filename, 'r') as f:
                saved = f.read()
            
            self.assertEqual(saved, content)


class TestColorFunctions(unittest.TestCase):
    """Test color output functions."""
    
    def test_colorize(self):
        """Test text colorization."""
        colored = colorize("test", Colors.GREEN)
        self.assertIn("test", colored)
        self.assertIn(Colors.GREEN, colored)
    
    def test_print_banner(self):
        """Test banner printing (no errors)."""
        # Just ensure no exceptions
        print_banner()


class TestModuleImports(unittest.TestCase):
    """Test that main module can be imported."""
    
    def test_import_main_module(self):
        """Test main module imports successfully."""
        try:
            import glm_researcher
            self.assertTrue(hasattr(glm_researcher, '__version__'))
            self.assertTrue(hasattr(glm_researcher, 'GLMClient'))
            self.assertTrue(hasattr(glm_researcher, 'AcademicPaperGenerator'))
        except ImportError as e:
            self.fail(f"Failed to import glm_researcher: {e}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
