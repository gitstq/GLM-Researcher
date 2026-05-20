# 🌐 Language Switcher | 语言切换 | 言語切替

[![简体中文](https://img.shields.io/badge/-简体中文-blue?style=flat-square)](README.md)
[![English](https://img.shields.io/badge/-English-red?style=flat-square)](README_EN.md)
[![繁體中文](https://img.shields.io/badge/-繁體中文-green?style=flat-square)](README_ZH_TW.md)
[![日本語](https://img.shields.io/badge/-日本語-orange?style=flat-square)](README_JA.md)

---

# 🔬 GLM-Researcher | 本地学术论文写作助手

> 🚀 **零依赖 · GLM-5.1驱动 · 本地运行 · 隐私安全**

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/yourusername/GLM-Researcher?style=flat-square)](https://github.com/yourusername/GLM-Researcher/stargazers)

---

## 🎉 项目介绍

**GLM-Researcher** 是一款轻量级本地学术论文写作助手，基于智谱AI的 **GLM-5.1** 大语言模型开发，支持 **128K上下文窗口**，可一次性处理超长文档。

### ✨ 核心价值

- 🔒 **隐私安全** - 所有数据本地处理，无需上传云端
- 💰 **成本可控** - 使用GLM-4-Flash高性价比模型
- 📦 **零依赖** - 仅需Python标准库，无需安装额外包
- 🎯 **专注学术** - 专为学术写作场景优化

### 🆚 自研差异化亮点

| 特性 | GLM-Researcher | 其他方案 |
|------|----------------|----------|
| 依赖要求 | **零依赖** | 需要安装多个包 |
| 部署方式 | **本地运行** | 需要API调用/云服务 |
| 上下文 | **128K** | 通常8K-32K |
| 离线能力 | **完整支持** | 受限 |
| 中国市场 | **原生支持** | 部分支持 |

---

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Zhipu AI API Key

### 安装步骤

```bash
# 克隆项目
git clone https://github.com/yourusername/GLM-Researcher.git
cd GLM-Researcher

# 设置API密钥
export ZHIPU_API_KEY="your-api-key-here"

# 运行设置脚本
chmod +x setup.sh
./setup.sh
```

### 快速使用

```bash
# 交互模式
python3 glm_researcher.py --interactive

# 生成摘要
python3 glm_researcher.py abstract --topic "人工智能在教育领域的应用" \
  --keywords "机器学习,教育,人工智能"

# 生成论文大纲
python3 glm_researcher.py outline --type empirical

# 生成文献综述
python3 glm_researcher.py lit-review --topic "深度学习研究" \
  --themes "理论基础" "前人研究" "方法论" "研究空白"

# 润色文稿
python3 glm_researcher.py polish --file ./my_draft.txt --style academic

# 生成参考文献
python3 glm_researcher.py references --topic "自然语言处理" --num 10
```

---

## 📖 详细使用指南

### 交互模式

启动交互式TUI界面：

```bash
python3 glm_researcher.py --interactive
```

```
glmr> help
Available Commands:
  abstract    - 生成论文摘要
  intro       - 生成引言部分
  lit-review  - 生成文献综述
  methodology - 生成方法论
  conclusion  - 生成结论
  polish      - 润色现有文本
  references  - 生成参考文献
  outline     - 显示论文大纲模板
  help        - 显示帮助信息
  exit        - 退出交互模式
```

### 命令详解

#### 📝 生成摘要
```bash
python3 glm_researcher.py abstract \
  --topic "区块链技术在供应链管理中的应用" \
  --keywords "区块链,供应链,智能合约" \
  --methodology "实证研究"
```

#### 📚 生成引言
```bash
python3 glm_researcher.py intro \
  --topic "区块链技术研究" \
  --questions "现有研究的局限性是什么?" \
              "本研究的创新点在哪里?" \
              "预期贡献是什么?"
```

#### 🔬 生成方法论
```bash
python3 glm_researcher.py methodology \
  --type quantitative \
  --subject "计算机科学"
```

### 配置管理

设置默认API密钥：
```bash
# 临时设置
export ZHIPU_API_KEY="your-api-key"

# 永久设置（添加到~/.bashrc或~/.zshrc）
echo 'export ZHIPU_API_KEY="your-api-key"' >> ~/.bashrc
```

### 常见问题

**Q: 提示API密钥无效？**
```bash
# 检查密钥是否正确设置
echo $ZHIPU_API_KEY

# 或直接传入密钥
python3 glm_researcher.py --api-key "your-key" abstract --topic "..."
```

**Q: 网络连接错误？**
```bash
# 检查网络连接
ping open.bigmodel.cn

# 或设置代理
export HTTP_PROXY="http://proxy:port"
export HTTPS_PROXY="http://proxy:port"
```

---

## 💡 设计思路与迭代规划

### 设计理念

1. **极简主义** - 零外部依赖，降低使用门槛
2. **隐私优先** - 数据本地处理，保护学术隐私
3. **学术规范** - 严格遵循APA/MLA等学术写作规范
4. **持续优化** - 基于用户反馈不断迭代改进

### 技术选型

| 组件 | 选型 | 原因 |
|------|------|------|
| 语言 | Python 3.8+ | 学术领域广泛使用 |
| 模型 | GLM-5.1 | 128K超长上下文 |
| API | Zhipu OpenAPI | 中国区访问稳定 |
| 无依赖 | urllib.request | Python标准库 |

### 后续迭代

- [ ] 📄 支持更多论文模板（IEEE、ACM、Nature等）
- [ ] 🌐 支持更多语言（中英日韩）
- [ ] 📊 添加图表生成功能
- [ ] 🔍 集成文献检索API
- [ ] 📝 支持LaTeX格式导出

---

## 📦 打包与部署

### 打包为独立可执行文件

使用PyInstaller打包：
```bash
pip install --break-system-packages pyinstaller
pyinstaller --onefile --name GLM-Researcher glm_researcher.py
```

### Docker部署

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN chmod +x setup.sh
ENV ZHIPU_API_KEY="your-api-key"
CMD ["python3", "glm_researcher.py", "--interactive"]
```

构建并运行：
```bash
docker build -t glm-researcher .
docker run -it glm-researcher
```

---

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

### 提交规范

```
feat: 新增论文模板
fix: 修复API调用问题
docs: 更新文档
refactor: 重构代码
test: 添加测试
```

### 开发流程

1. Fork项目
2. 创建特性分支 `git checkout -b feature/AmazingFeature`
3. 提交更改 `git commit -m 'Add some AmazingFeature'`
4. 推送到分支 `git push origin feature/AmazingFeature`
5. 创建Pull Request

---

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源。

---

## 🙏 致谢

- [Zhipu AI](https://www.zhipuai.cn/) - 提供GLM-5.1大语言模型API
- 所有贡献者和用户

---

<p align="center">
  <strong>Made with ❤️ for researchers worldwide</strong><br>
  🔬 GLM-Researcher - 让学术写作更简单
</p>
