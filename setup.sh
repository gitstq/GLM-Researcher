#!/bin/bash
# GLM-Researcher - Quick Start Script
# Usage: ./setup.sh

set -e

echo "🔬 GLM-Researcher Setup"
echo "======================"

# Check Python version
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+' | head -1)
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.8+ is required. Found: Python $python_version"
    exit 1
fi

echo "✅ Python version: $python_version"

# Make scripts executable
chmod +x glm_researcher.py
chmod +x src/glm_researcher.py

echo "✅ Scripts made executable"

# Check for API key
if [ -z "$ZHIPU_API_KEY" ]; then
    echo ""
    echo "⚠️  ZHIPU_API_KEY not set"
    echo ""
    echo "To get your API key:"
    echo "1. Visit https://open.bigmodel.cn/"
    echo "2. Register an account"
    echo "3. Create a new API key"
    echo ""
    echo "Then set it with:"
    echo "  export ZHIPU_API_KEY='your-api-key-here'"
    echo ""
    echo "Or pass it directly:"
    echo "  python3 glm_researcher.py --api-key YOUR_API_KEY abstract --topic 'Your Topic'"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Quick Start:"
echo "  python3 glm_researcher.py --interactive"
echo "  python3 glm_researcher.py abstract --topic 'AI in Education'"
echo "  python3 glm_researcher.py outline --type empirical"
echo ""
