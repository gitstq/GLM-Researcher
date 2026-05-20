# Contributing to GLM-Researcher

Thank you for your interest in contributing to GLM-Researcher! 🎉

This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Bugs

Before submitting a bug report:
1. Check existing issues to avoid duplicates
2. Provide a clear title and description
3. Include steps to reproduce the issue
4. Add your environment info (Python version, OS, etc.)

### Suggesting Features

We welcome feature suggestions! Please:
1. Check existing issues and pull requests
2. Describe the feature and its potential benefits
3. Provide use case examples

### Pull Requests

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit:
   ```bash
   git commit -m 'Add some amazing feature'
   ```

4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a Pull Request

### Commit Message Format

We follow the Angular commit convention:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### Coding Standards

- Write clean, readable code
- Add docstrings to functions and classes
- Include type hints where appropriate
- Keep functions focused and small
- Write meaningful variable and function names

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GLM-Researcher.git
   cd GLM-Researcher
   ```

2. Install development dependencies:
   ```bash
   pip install --break-system-packages pytest black flake8
   ```

3. Run tests:
   ```bash
   python3 -m pytest tests/ -v
   ```

4. Format code:
   ```bash
   black src/ tests/
   ```

## Questions?

Feel free to:
- Open an issue for questions
- Join our discussions
- Contact the maintainers

Thank you for making GLM-Researcher better! 🙏
