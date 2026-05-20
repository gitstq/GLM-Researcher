# 🌐 Language Switcher | 语言切换 | 言語切替

[![简体中文](https://img.shields.io/badge/-简体中文-blue?style=flat-square)](README.md)
[![English](https://img.shields.io/badge/-English-red?style=flat-square)](README_EN.md)
[![繁體中文](https://img.shields.io/badge/-繁體中文-green?style=flat-square)](README_ZH_TW.md)
[![日本語](https://img.shields.io/badge/-日本語-orange?style=flat-square)](README_JA.md)

---

# 🔬 GLM-Researcher | Local Academic Research Writing Assistant

> 🚀 **Zero Dependencies · Powered by GLM-5.1 · Local Execution · Privacy First**

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/yourusername/GLM-Researcher?style=flat-square)](https://github.com/yourusername/GLM-Researcher/stargazers)

---

## 🎉 Introduction

**GLM-Researcher** is a lightweight, zero-dependency academic research writing assistant powered by Zhipu AI's **GLM-5.1** large language model, featuring a massive **128K context window** for processing ultra-long documents.

### ✨ Core Values

- 🔒 **Privacy First** - All data processed locally, no cloud upload
- 💰 **Cost Effective** - Using GLM-4-Flash cost-efficient model
- 📦 **Zero Dependencies** - Python standard library only, no extra packages needed
- 🎯 **Academic Focused** - Optimized for academic writing scenarios

### 🆚 Differentiation Highlights

| Feature | GLM-Researcher | Other Solutions |
|---------|---------------|-----------------|
| Dependencies | **Zero** | Multiple packages required |
| Deployment | **Local** | API calls/Cloud needed |
| Context | **128K** | Usually 8K-32K |
| Offline | **Full Support** | Limited |
| China Market | **Native Support** | Partial Support |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Zhipu AI API Key

### Installation

```bash
# Clone the project
git clone https://github.com/yourusername/GLM-Researcher.git
cd GLM-Researcher

# Set your API key
export ZHIPU_API_KEY="your-api-key-here"

# Run setup script
chmod +x setup.sh
./setup.sh
```

### Quick Usage

```bash
# Interactive mode
python3 glm_researcher.py --interactive

# Generate abstract
python3 glm_researcher.py abstract --topic "AI Applications in Education" \
  --keywords "machine learning,education,artificial intelligence"

# Generate paper outline
python3 glm_researcher.py outline --type empirical

# Generate literature review
python3 glm_researcher.py lit-review --topic "Deep Learning Research" \
  --themes "theoretical foundations" "prior research" "methodology" "research gaps"

# Polish prose
python3 glm_researcher.py polish --file ./my_draft.txt --style academic

# Generate references
python3 glm_researcher.py references --topic "Natural Language Processing" --num 10
```

---

## 📖 Detailed Usage Guide

### Interactive Mode

Launch the interactive TUI interface:

```bash
python3 glm_researcher.py --interactive
```

```
glmr> help
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
```

### Command Reference

#### 📝 Generate Abstract
```bash
python3 glm_researcher.py abstract \
  --topic "Blockchain Applications in Supply Chain Management" \
  --keywords "blockchain,supply chain,smart contracts" \
  --methodology "empirical research"
```

#### 📚 Generate Introduction
```bash
python3 glm_researcher.py intro \
  --topic "Blockchain Technology Research" \
  --questions "What are the limitations of existing research?" \
              "What are the innovations of this study?" \
              "What are the expected contributions?"
```

#### 🔬 Generate Methodology
```bash
python3 glm_researcher.py methodology \
  --type quantitative \
  --subject "Computer Science"
```

### Configuration

Set default API key:
```bash
# Temporary
export ZHIPU_API_KEY="your-api-key"

# Permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export ZHIPU_API_KEY="your-api-key"' >> ~/.bashrc
```

### Troubleshooting

**Q: API key invalid?**
```bash
# Check if key is set correctly
echo $ZHIPU_API_KEY

# Or pass key directly
python3 glm_researcher.py --api-key "your-key" abstract --topic "..."
```

**Q: Network error?**
```bash
# Check network
ping open.bigmodel.cn

# Or set proxy
export HTTP_PROXY="http://proxy:port"
export HTTPS_PROXY="http://proxy:port"
```

---

## 💡 Design Philosophy & Roadmap

### Design Principles

1. **Minimalism** - Zero external dependencies, lower barrier to entry
2. **Privacy First** - Local data processing, protecting academic privacy
3. **Academic Standards** - Strictly following APA/MLA academic writing conventions
4. **Continuous Improvement** - Iterating based on user feedback

### Technology Choices

| Component | Choice | Reason |
|-----------|--------|--------|
| Language | Python 3.8+ | Widely used in academia |
| Model | GLM-5.1 | 128K ultra-long context |
| API | Zhipu OpenAPI | Stable access in China |
| No Dependencies | urllib.request | Python standard library |

### Future Roadmap

- [ ] 📄 Support more paper templates (IEEE, ACM, Nature, etc.)
- [ ] 🌐 Support more languages (EN, ZH, JA, KO)
- [ ] 📊 Add chart/diagram generation
- [ ] 🔍 Integrate literature search API
- [ ] 📝 Support LaTeX export

---

## 📦 Packaging & Deployment

### Package as Standalone Executable

Using PyInstaller:
```bash
pip install --break-system-packages pyinstaller
pyinstaller --onefile --name GLM-Researcher glm_researcher.py
```

### Docker Deployment

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN chmod +x setup.sh
ENV ZHIPU_API_KEY="your-api-key"
CMD ["python3", "glm_researcher.py", "--interactive"]
```

Build and run:
```bash
docker build -t glm-researcher .
docker run -it glm-researcher
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit Issues and Pull Requests.

### Commit Convention

```
feat: Add new paper template
fix: Fix API call issues
docs: Update documentation
refactor: Refactor code
test: Add tests
```

### Development Workflow

1. Fork the project
2. Create your feature branch `git checkout -b feature/AmazingFeature`
3. Commit your changes `git commit -m 'Add some AmazingFeature'`
4. Push to the branch `git push origin feature/AmazingFeature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [Zhipu AI](https://www.zhipuai.cn/) - Providing GLM-5.1 LLM API
- All contributors and users

---

<p align="center">
  <strong>Made with ❤️ for researchers worldwide</strong><br>
  🔬 GLM-Researcher - Making Academic Writing Simpler
</p>
