#!/usr/bin/env python3
"""
GLM-Researcher - Local Academic Research Assistant powered by GLM-5.1
======================================================================

A lightweight, zero-dependency academic research writing assistant CLI tool
powered by Zhipu AI's GLM-5.1 model with 128K context window.

Author: GLM-Researcher Team
License: MIT
"""

import json
import sys
import os
from pathlib import Path
from typing import Optional, Dict, List, Any
import argparse
import urllib.request
import urllib.parse
import urllib.error
import re
import hashlib

__version__ = "1.0.0"
__author__ = "GLM-Researcher Team"

# ANSI Color Codes for TUI
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colorize(text: str, color: str) -> str:
    """Add ANSI color codes to text."""
    return f"{color}{text}{Colors.ENDC}"

def print_banner():
    """Print the application banner."""
    banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   {Colors.BOLD}🔬 GLM-Researcher v{__version__}{Colors.ENDC}{Colors.CYAN}                                   ║
║   {Colors.YELLOW}Local Academic Research Writing Assistant{Colors.ENDC}{Colors.CYAN}                  ║
║   {Colors.GREEN}Powered by GLM-5.1 (128K Context Window){Colors.ENDC}{Colors.CYAN}                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Colors.ENDC}
    """
    print(banner)

def print_success(message: str):
    """Print success message."""
    print(f"{Colors.GREEN}✅ {message}{Colors.ENDC}")

def print_error(message: str):
    """Print error message."""
    print(f"{Colors.RED}❌ {message}{Colors.ENDC}")

def print_info(message: str):
    """Print info message."""
    print(f"{Colors.CYAN}ℹ️  {message}{Colors.ENDC}")

def print_warning(message: str):
    """Print warning message."""
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.ENDC}")

def print_step(step: int, total: int, message: str):
    """Print step progress."""
    print(f"{Colors.BLUE}[{step}/{total}]{Colors.ENDC} {message}")

class GLMClient:
    """Client for Zhipu AI GLM API."""
    
    BASE_URL = "https://open.bigmodel.cn/api/paas/v4"
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize GLM client.
        
        Args:
            api_key: Zhipu AI API key. If None, reads from environment.
        """
        self.api_key = api_key or os.environ.get("ZHIPU_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Set ZHIPU_API_KEY environment variable or pass --api-key")
    
    def chat(self, messages: List[Dict], model: str = "glm-4-flash", 
             temperature: float = 0.7, max_tokens: int = 2048) -> str:
        """Send chat request to GLM API.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            model: Model name (default: glm-4-flash for cost efficiency)
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens in response
            
        Returns:
            Response content as string
        """
        url = f"{self.BASE_URL}/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode('utf-8'),
                headers=headers,
                method='POST'
            )
            
            with urllib.request.urlopen(req, timeout=120) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result['choices'][0]['message']['content']
                
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8') if e.fp else "{}"
            try:
                error_json = json.loads(error_body)
                raise Exception(f"API Error {e.code}: {error_json.get('error', {}).get('message', str(e))}")
            except json.JSONDecodeError:
                raise Exception(f"API Error {e.code}: {error_body[:500]}")
        except urllib.error.URLError as e:
            raise Exception(f"Network Error: {e.reason}")
        except Exception as e:
            raise Exception(f"Request failed: {str(e)}")

class AcademicPaperGenerator:
    """Generate academic paper sections using GLM-5.1."""
    
    SYSTEM_PROMPT = """You are an expert academic research assistant powered by GLM-5.1.
You help researchers write high-quality academic papers with proper structure,
clear arguments, and rigorous methodology. Always follow academic writing
conventions and provide well-reasoned, evidence-based content."""
    
    def __init__(self, client: GLMClient):
        """Initialize paper generator.
        
        Args:
            client: GLM API client instance
        """
        self.client = client
    
    def generate_abstract(self, topic: str, keywords: List[str], 
                         methodology: str = "empirical research") -> str:
        """Generate paper abstract.
        
        Args:
            topic: Research topic/title
            keywords: List of keywords
            methodology: Research methodology
            
        Returns:
            Generated abstract text
        """
        prompt = f"""Write a comprehensive academic abstract (200-300 words) for a paper on:

Topic: {topic}
Keywords: {', '.join(keywords)}
Methodology: {methodology}

The abstract should:
1. State the research problem and motivation
2. Briefly describe the methodology
3. Summarize key findings or contributions
4. Highlight the significance and implications

Write in formal academic style, third person, past tense for findings."""
        
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        
        return self.client.chat(messages, model="glm-4-flash", temperature=0.7)
    
    def generate_introduction(self, topic: str, research_questions: List[str]) -> str:
        """Generate paper introduction section.
        
        Args:
            topic: Research topic
            research_questions: List of research questions
            
        Returns:
            Generated introduction text
        """
        questions_text = "\n".join([f"- {q}" for q in research_questions])
        
        prompt = f"""Write a comprehensive introduction section for an academic paper on:

Topic: {topic}

Research Questions:
{questions_text}

Structure the introduction as follows:
1. Opening/Hook - Start with the broader context and significance
2. Background - Provide necessary context for understanding the research
3. Literature Gap - Identify what's missing in current research
4. Research Contribution - State your paper's unique contributions
5. Paper Structure - Briefly outline the remaining sections

Use approximately 800-1000 words. Maintain academic tone and style."""
        
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        
        return self.client.chat(messages, model="glm-4-flash", temperature=0.7)
    
    def generate_literature_review(self, topic: str, themes: List[str]) -> str:
        """Generate literature review section.
        
        Args:
            topic: Research topic
            themes: Key themes to cover
            
        Returns:
            Generated literature review text
        """
        themes_text = "\n".join([f"- {t}" for t in themes])
        
        prompt = f"""Write a structured literature review for a paper on:

Topic: {topic}

Key Themes to Cover:
{themes_text}

Structure the literature review as:
1. Introduction to the research area
2. Theme 1 - [detailed discussion with hypothetical citations]
3. Theme 2 - [detailed discussion with hypothetical citations]
4. Theme 3 - [detailed discussion with hypothetical citations]
5. Synthesis and Research Gap

Note: Use hypothetical citations like (Author, Year) format.
Aim for 1000-1200 words with proper academic transitions."""
        
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        
        return self.client.chat(messages, model="glm-4-flash", temperature=0.7)
    
    def generate_methodology(self, research_type: str, subject_area: str) -> str:
        """Generate methodology section.
        
        Args:
            research_type: Type of research (qualitative, quantitative, mixed)
            subject_area: Subject area
            
        Returns:
            Generated methodology text
        """
        prompt = f"""Write a comprehensive methodology section for:

Research Type: {research_type}
Subject Area: {subject_area}

Structure the methodology section as:
1. Research Design Overview
2. Data Collection Methods
3. Data Analysis Techniques
4. Validity and Reliability Measures
5. Ethical Considerations

Include specific details appropriate for {research_type} research in {subject_area}.
Aim for 800-1000 words with sufficient detail for replication."""
        
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        
        return self.client.chat(messages, model="glm-4-flash", temperature=0.7)
    
    def generate_conclusion(self, topic: str, key_findings: List[str],
                           limitations: List[str], future_work: List[str]) -> str:
        """Generate conclusion section.
        
        Args:
            topic: Research topic
            key_findings: List of key findings
            limitations: List of limitations
            future_work: List of future research directions
            
        Returns:
            Generated conclusion text
        """
        findings_text = "\n".join([f"- {f}" for f in key_findings])
        limitations_text = "\n".join([f"- {l}" for l in limitations])
        future_text = "\n".join([f"- {f}" for f in future_work])
        
        prompt = f"""Write a compelling conclusion section for a paper on:

Topic: {topic}

Key Findings:
{findings_text}

Limitations:
{limitations_text}

Future Research Directions:
{future_text}

Structure the conclusion as:
1. Summary of Research
2. Key Findings Overview
3. Theoretical and Practical Implications
4. Limitations
5. Future Research Directions

Aim for 600-800 words, emphasizing contributions and significance."""
        
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        
        return self.client.chat(messages, model="glm-4-flash", temperature=0.7)
    
    def polish_prose(self, text: str, style: str = "academic") -> str:
        """Polish and improve existing prose.
        
        Args:
            text: Text to polish
            style: Writing style (academic, formal, simple)
            
        Returns:
            Polished text
        """
        prompt = f"""Polish and improve the following text to enhance clarity, 
coherence, and academic quality:

Original Text:
{text}

Style Target: {style}

Improve the text by:
1. Enhancing clarity and precision
2. Improving flow and transitions
3. Strengthening arguments
4. Maintaining academic tone
5. Fixing any grammatical issues

Return only the polished version without explanations."""
        
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        
        return self.client.chat(messages, model="glm-4-flash", temperature=0.6)
    
    def generate_references(self, topic: str, num_refs: int = 10) -> str:
        """Generate hypothetical references list.
        
        Args:
            topic: Research topic
            num_refs: Number of references to generate
            
        Returns:
            Formatted references in APA style
        """
        prompt = f"""Generate {num_refs} academic references in APA 7th edition format
for a paper on: {topic}

Include a mix of:
- Journal articles
- Conference papers
- Books/chapters
- Online sources

Use realistic but hypothetical citations. Format strictly according to APA 7th edition.
Return only the references list, numbered."""
        
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        
        return self.client.chat(messages, model="glm-4-flash", temperature=0.8)

class CitationChecker:
    """Check and format academic citations."""
    
    @staticmethod
    def extract_citations(text: str) -> List[str]:
        """Extract citations from text.
        
        Args:
            text: Text containing citations
            
        Returns:
            List of extracted citations
        """
        # Pattern for various citation formats
        patterns = [
            r'\(([A-Z][a-z]+(?:\s+(?:et\s+al\.|[A-Z][a-z]+))?(?:,\s*\d{4}[a-z]?(?:,\s*p\.\s*\d+(?:-\d+)?)?)?)\)',  # (Author, Year, p. X)
            r'\[(\d+(?:,\s*\d+)*)\]',  # [1] or [1, 2, 3]
            r'([A-Z][a-z]+(?:\s+(?:et\s+al\.|[A-Z][a-z]+))?,\s*\d{4})',  # Author, Year
        ]
        
        citations = []
        for pattern in patterns:
            matches = re.findall(pattern, text)
            citations.extend(matches)
        
        return list(set(citations))
    
    @staticmethod
    def format_apa(author: str, year: str, title: str, source: str, 
                   doi: str = "", pages: str = "") -> str:
        """Format a reference in APA 7th edition style.
        
        Args:
            author: Author name(s)
            year: Publication year
            title: Work title
            source: Journal or source name
            doi: DOI if available
            pages: Page numbers
            
        Returns:
            Formatted APA reference
        """
        ref = f"{author} ({year}). {title}. {source}"
        if pages:
            ref += f", {pages}"
        if doi:
            ref += f". https://doi.org/{doi}"
        return ref
    
    @staticmethod
    def validate_citation_format(citation: str) -> Dict[str, Any]:
        """Validate citation format.
        
        Args:
            citation: Citation string to validate
            
        Returns:
            Dict with validation results
        """
        result = {
            "valid": False,
            "issues": [],
            "suggestion": None
        }
        
        # Check for basic components
        has_author = bool(re.search(r'[A-Z][a-z]+', citation))
        has_year = bool(re.search(r'\d{4}', citation))
        
        if not has_author:
            result["issues"].append("Missing author name")
        if not has_year:
            result["issues"].append("Missing publication year")
        
        result["valid"] = has_author and has_year
        return result

class PaperOutlineGenerator:
    """Generate paper outlines and structures."""
    
    STRUCTURE_TEMPLATES = {
        "empirical": {
            "name": "Empirical Research Paper",
            "sections": [
                "1. Abstract",
                "2. Introduction",
                "   2.1 Background",
                "   2.2 Research Questions/Hypotheses",
                "   2.3 Contributions",
                "3. Literature Review",
                "   3.1 Theoretical Framework",
                "   3.2 Prior Empirical Work",
                "   3.3 Research Gap",
                "4. Methodology",
                "   4.1 Research Design",
                "   4.2 Data Collection",
                "   4.3 Data Analysis",
                "   4.4 Validity Measures",
                "5. Results",
                "   5.1 Descriptive Statistics",
                "   5.2 Hypothesis Testing",
                "   5.3 Additional Analyses",
                "6. Discussion",
                "   6.1 Interpretation of Findings",
                "   6.2 Implications",
                "   6.3 Limitations",
                "7. Conclusion",
                "8. References",
                "9. Appendices"
            ]
        },
        "theoretical": {
            "name": "Theoretical/Conceptual Paper",
            "sections": [
                "1. Abstract",
                "2. Introduction",
                "   2.1 Problem Statement",
                "   2.2 Objectives",
                "3. Theoretical Background",
                "   3.1 Core Concepts",
                "   3.2 Theoretical Foundations",
                "   3.3 Conceptual Framework",
                "4. Theoretical Development",
                "   4.1 Propositions",
                "   4.2 Theoretical Model",
                "5. Discussion",
                "   5.1 Implications for Theory",
                "   5.2 Practical Implications",
                "   5.3 Limitations",
                "6. Conclusion",
                "7. References"
            ]
        },
        "review": {
            "name": "Literature Review Paper",
            "sections": [
                "1. Abstract",
                "2. Introduction",
                "   2.1 Review Scope and Objectives",
                "   2.2 Research Questions",
                "3. Methodology",
                "   3.1 Search Strategy",
                "   3.2 Selection Criteria",
                "   3.3 Data Extraction",
                "4. Results",
                "   4.1 Overview of Studies",
                "   4.2 Thematic Analysis",
                "   4.3 Key Findings by Theme",
                "5. Discussion",
                "   5.1 Synthesis",
                "   5.2 Research Gaps",
                "   5.3 Future Directions",
                "6. Conclusion",
                "7. References"
            ]
        }
    }
    
    @classmethod
    def get_template(cls, research_type: str) -> Dict:
        """Get outline template for research type.
        
        Args:
            research_type: Type of research
            
        Returns:
            Template dictionary
        """
        return cls.STRUCTURE_TEMPLATES.get(
            research_type.lower(),
            cls.STRUCTURE_TEMPLATES["empirical"]
        )
    
    @classmethod
    def list_templates(cls) -> List[str]:
        """List available template names.
        
        Returns:
            List of template names
        """
        return list(cls.STRUCTURE_TEMPLATES.keys())

def save_to_file(content: str, filename: str, output_dir: str = ".") -> str:
    """Save content to file.
    
    Args:
        content: Content to save
        filename: Output filename
        output_dir: Output directory
        
    Returns:
        Full path to saved file
    """
    output_path = Path(output_dir) / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return str(output_path.absolute())

def interactive_mode(client: GLMClient):
    """Run interactive TUI mode.
    
    Args:
        client: GLM API client instance
    """
    generator = AcademicPaperGenerator(client)
    
    print_info("Welcome to Interactive Mode!")
    print("Type 'help' for available commands, 'exit' to quit.\n")
    
    while True:
        try:
            command = input(f"{Colors.CYAN}glmr> {Colors.ENDC}").strip()
            
            if not command:
                continue
            
            if command.lower() in ['exit', 'quit', 'q']:
                print_success("Thank you for using GLM-Researcher!")
                break
            
            if command.lower() == 'help':
                print("""
Available Commands:
  abstract    - Generate paper abstract
  intro       - Generate introduction section
  lit-review  - Generate literature review
  methodology - Generate methodology section
  conclusion  - Generate conclusion section
  polish      - Polish existing text
  references  - Generate references list
  outline     - Show paper outline templates
  help        - Show this help message
  exit        - Exit interactive mode
                """)
                continue
            
            if command.lower() == 'outline':
                print("\nAvailable Outline Templates:")
                for name in generator.client and PaperOutlineGenerator.list_templates():
                    template = PaperOutlineGenerator.get_template(name)
                    print(f"\n{Colors.GREEN}{template['name']} ({name}){Colors.ENDC}")
                    for section in template['sections'][:10]:
                        print(f"  {section}")
                    print("  ...")
                print()
                continue
            
            if command.lower() == 'abstract':
                topic = input("Research topic: ").strip()
                keywords = input("Keywords (comma-separated): ").strip()
                if keywords:
                    keywords = [k.strip() for k in keywords.split(',')]
                else:
                    keywords = []
                methodology = input("Methodology [empirical]: ").strip() or "empirical research"
                
                print_info("Generating abstract...")
                result = generator.generate_abstract(topic, keywords, methodology)
                print(f"\n{Colors.GREEN}{'='*60}{Colors.ENDC}")
                print(result)
                print(f"{Colors.GREEN}{'='*60}{Colors.ENDC}\n")
                continue
            
            if command.lower() == 'references':
                topic = input("Research topic: ").strip()
                num = input("Number of references [10]: ").strip()
                num_refs = int(num) if num.isdigit() else 10
                
                print_info("Generating references...")
                result = generator.generate_references(topic, num_refs)
                print(f"\n{Colors.GREEN}{'='*60}{Colors.ENDC}")
                print(result)
                print(f"{Colors.GREEN}{'='*60}{Colors.ENDC}\n")
                continue
            
            print_warning(f"Unknown command: {command}")
            print_info("Type 'help' for available commands.")
            
        except KeyboardInterrupt:
            print("\n")
            print_success("Thank you for using GLM-Researcher!")
            break
        except Exception as e:
            print_error(f"Error: {str(e)}")

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="GLM-Researcher: Local Academic Research Writing Assistant powered by GLM-5.1",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate abstract
  python glm_researcher.py abstract --topic "AI in Education" --keywords "machine learning,education,AI"
  
  # Generate introduction
  python glm_researcher.py intro --topic "Machine Learning Applications"
  
  # Interactive mode
  python glm_researcher.py --interactive
  
  # With API key
  python glm_researcher.py --api-key YOUR_API_KEY abstract --topic "Research Topic"

Environment Variables:
  ZHIPU_API_KEY    Your Zhipu AI API key (required)

For more information, visit: https://github.com/yourusername/GLM-Researcher
        """
    )
    
    parser.add_argument('--api-key', '-k', 
                       help="Zhipu AI API key (or set ZHIPU_API_KEY env var)")
    parser.add_argument('--model', '-m', default='glm-4-flash',
                       help="GLM model to use (default: glm-4-flash)")
    parser.add_argument('--output', '-o', default='.',
                       help="Output directory for generated content")
    parser.add_argument('--interactive', '-i', action='store_true',
                       help="Start interactive TUI mode")
    parser.add_argument('--version', '-v', action='version',
                       version=f'GLM-Researcher v{__version__}')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Abstract command
    abstract_parser = subparsers.add_parser('abstract', help='Generate paper abstract')
    abstract_parser.add_argument('--topic', '-t', required=True, help='Research topic')
    abstract_parser.add_argument('--keywords', '-k', help='Comma-separated keywords')
    abstract_parser.add_argument('--methodology', '-m', default='empirical research',
                                help='Research methodology')
    
    # Introduction command
    intro_parser = subparsers.add_parser('intro', help='Generate introduction section')
    intro_parser.add_argument('--topic', '-t', required=True, help='Research topic')
    intro_parser.add_argument('--questions', '-q', nargs='+', help='Research questions')
    
    # Literature review command
    lit_parser = subparsers.add_parser('lit-review', help='Generate literature review')
    lit_parser.add_argument('--topic', '-t', required=True, help='Research topic')
    lit_parser.add_argument('--themes', '-T', nargs='+', help='Key themes to cover')
    
    # Methodology command
    method_parser = subparsers.add_parser('methodology', help='Generate methodology section')
    method_parser.add_argument('--type', '-t', default='quantitative',
                              choices=['qualitative', 'quantitative', 'mixed'],
                              help='Research type')
    method_parser.add_argument('--subject', '-s', required=True, help='Subject area')
    
    # Conclusion command
    concl_parser = subparsers.add_parser('conclusion', help='Generate conclusion section')
    concl_parser.add_argument('--topic', '-t', required=True, help='Research topic')
    concl_parser.add_argument('--findings', '-f', nargs='+', help='Key findings')
    concl_parser.add_argument('--limitations', '-l', nargs='+', help='Limitations')
    concl_parser.add_argument('--future', help='Future work directions')
    
    # Polish command
    polish_parser = subparsers.add_parser('polish', help='Polish existing text')
    polish_parser.add_argument('--file', '-f', help='File to polish')
    polish_parser.add_argument('--text', '-t', help='Text to polish')
    polish_parser.add_argument('--style', '-s', default='academic',
                             choices=['academic', 'formal', 'simple'],
                             help='Writing style')
    
    # References command
    ref_parser = subparsers.add_parser('references', help='Generate references')
    ref_parser.add_argument('--topic', '-t', required=True, help='Research topic')
    ref_parser.add_argument('--num', '-n', type=int, default=10, help='Number of references')
    
    # Outline command
    outline_parser = subparsers.add_parser('outline', help='Show paper outline')
    outline_parser.add_argument('--type', '-t', default='empirical',
                                choices=['empirical', 'theoretical', 'review'],
                                help='Research type')
    
    args = parser.parse_args()
    
    print_banner()
    
    try:
        # Initialize client
        api_key = args.api_key or os.environ.get("ZHIPU_API_KEY")
        if not api_key:
            print_error("API key required. Set ZHIPU_API_KEY or use --api-key")
            sys.exit(1)
        
        client = GLMClient(api_key)
        generator = AcademicPaperGenerator(client)
        
        if args.interactive or not args.command:
            interactive_mode(client)
            return
        
        # Process commands
        if args.command == 'abstract':
            keywords = []
            if args.keywords:
                keywords = [k.strip() for k in args.keywords.split(',')]
            
            print_step(1, 1, f"Generating abstract for: {args.topic}")
            result = generator.generate_abstract(args.topic, keywords, args.methodology)
            
            filename = save_to_file(result, "abstract.md", args.output)
            print_success(f"Abstract saved to: {filename}")
            print(f"\n{Colors.YELLOW}{'='*60}{Colors.ENDC}")
            print(result)
            print(f"{Colors.YELLOW}{'='*60}{Colors.ENDC}")
        
        elif args.command == 'intro':
            questions = args.questions or ["What is the current state of research?",
                                          "What gaps exist?",
                                          "How does this study contribute?"]
            
            print_step(1, 1, f"Generating introduction for: {args.topic}")
            result = generator.generate_introduction(args.topic, questions)
            
            filename = save_to_file(result, "introduction.md", args.output)
            print_success(f"Introduction saved to: {filename}")
            print(f"\n{Colors.YELLOW}{'='*60}{Colors.ENDC}")
            print(result)
            print(f"{Colors.YELLOW}{'='*60}{Colors.ENDC}")
        
        elif args.command == 'lit-review':
            themes = args.themes or ["theoretical foundations", "prior research",
                                    "methodological approaches", "research gaps"]
            
            print_step(1, 1, f"Generating literature review for: {args.topic}")
            result = generator.generate_literature_review(args.topic, themes)
            
            filename = save_to_file(result, "literature_review.md", args.output)
            print_success(f"Literature review saved to: {filename}")
            print(f"\n{Colors.YELLOW}{'='*60}{Colors.ENDC}")
            print(result)
            print(f"{Colors.YELLOW}{'='*60}{Colors.ENDC}")
        
        elif args.command == 'methodology':
            print_step(1, 1, f"Generating methodology for: {args.subject}")
            result = generator.generate_methodology(args.type, args.subject)
            
            filename = save_to_file(result, "methodology.md", args.output)
            print_success(f"Methodology saved to: {filename}")
            print(f"\n{Colors.YELLOW}{'='*60}{Colors.ENDC}")
            print(result)
            print(f"{Colors.YELLOW}{'='*60}{Colors.ENDC}")
        
        elif args.command == 'conclusion':
            findings = args.findings or ["Key finding 1", "Key finding 2"]
            limitations = args.limitations or ["Sample size limitations",
                                              "Generalizability constraints"]
            future = args.future or ["Further validation needed",
                                    "Explore additional contexts"]
            
            print_step(1, 1, f"Generating conclusion for: {args.topic}")
            result = generator.generate_conclusion(args.topic, findings, limitations, future)
            
            filename = save_to_file(result, "conclusion.md", args.output)
            print_success(f"Conclusion saved to: {filename}")
            print(f"\n{Colors.YELLOW}{'='*60}{Colors.ENDC}")
            print(result)
            print(f"{Colors.YELLOW}{'='*60}{Colors.ENDC}")
        
        elif args.command == 'polish':
            if args.file:
                with open(args.file, 'r', encoding='utf-8') as f:
                    text = f.read()
            elif args.text:
                text = args.text
            else:
                print_error("Please provide --file or --text argument")
                sys.exit(1)
            
            print_step(1, 1, "Polishing text...")
            result = generator.polish_prose(text, args.style)
            
            filename = save_to_file(result, "polished.md", args.output)
            print_success(f"Polished text saved to: {filename}")
            print(f"\n{Colors.YELLOW}{'='*60}{Colors.ENDC}")
            print(result)
            print(f"{Colors.YELLOW}{'='*60}{Colors.ENDC}")
        
        elif args.command == 'references':
            print_step(1, 1, f"Generating {args.num} references for: {args.topic}")
            result = generator.generate_references(args.topic, args.num)
            
            filename = save_to_file(result, "references.md", args.output)
            print_success(f"References saved to: {filename}")
            print(f"\n{Colors.YELLOW}{'='*60}{Colors.ENDC}")
            print(result)
            print(f"{Colors.YELLOW}{'='*60}{Colors.ENDC}")
        
        elif args.command == 'outline':
            template = PaperOutlineGenerator.get_template(args.type)
            print(f"\n{Colors.GREEN}{'='*60}{Colors.ENDC}")
            print(f"Paper Outline: {template['name']}")
            print(f"{Colors.GREEN}{'='*60}{Colors.ENDC}\n")
            for section in template['sections']:
                print(section)
            print()
    
    except KeyboardInterrupt:
        print("\n")
        print_warning("Operation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print_error(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
