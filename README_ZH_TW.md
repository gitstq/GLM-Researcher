# 🌐 Language Switcher | 語言切換 | 言語切替

[![简体中文](https://img.shields.io/badge/-简体中文-blue?style=flat-square)](README.md)
[![English](https://img.shields.io/badge/-English-red?style=flat-square)](README_EN.md)
[![繁體中文](https://img.shields.io/badge/-繁體中文-green?style=flat-square)](README_ZH_TW.md)
[![日本語](https://img.shields.io/badge/-日本語-orange?style=flat-square)](README_JA.md)

---

# 🔬 GLM-Researcher | 本地學術論文寫作助手

> 🚀 **零依賴 · GLM-5.1驅動 · 本地運行 · 隱私安全**

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/yourusername/GLM-Researcher?style=flat-square)](https://github.com/yourusername/GLM-Researcher/stargazers)

---

## 🎉 專案介紹

**GLM-Researcher** 是一款輕量級本地學術論文寫作助手，基於智譜AI的 **GLM-5.1** 大語言模型開發，支援 **128K上下文窗口**，可一次性處理超長文檔。

### ✨ 核心價值

- 🔒 **隱私安全** - 所有數據本地處理，無需上傳雲端
- 💰 **成本可控** - 使用GLM-4-Flash高性價比模型
- 📦 **零依賴** - 僅需Python標準庫，無需安裝額外套件
- 🎯 **專注學術** - 專為學術寫作場景優化

### 🆚 自研差異化亮點

| 特性 | GLM-Researcher | 其他方案 |
|------|----------------|----------|
| 依賴要求 | **零依賴** | 需要安裝多個套件 |
| 部署方式 | **本地運行** | 需要API調用/雲服務 |
| 上下文 | **128K** | 通常8K-32K |
| 離線能力 | **完整支援** | 受限 |
| 中國市場 | **原生支援** | 部分支援 |

---

## 🚀 快速開始

### 環境要求

- Python 3.8+
- 智譜AI API Key

### 安裝步驟

```bash
# 克隆專案
git clone https://github.com/yourusername/GLM-Researcher.git
cd GLM-Researcher

# 設定API密鑰
export ZHIPU_API_KEY="your-api-key-here"

# 執行設定腳本
chmod +x setup.sh
./setup.sh
```

### 快速使用

```bash
# 互動模式
python3 glm_researcher.py --interactive

# 生成摘要
python3 glm_researcher.py abstract --topic "人工智慧在教育領域的應用" \
  --keywords "機器學習,教育,人工智慧"

# 生成論文大綱
python3 glm_researcher.py outline --type empirical

# 生成文獻綜述
python3 glm_researcher.py lit-review --topic "深度學習研究" \
  --themes "理論基礎" "前人研究" "方法論" "研究空白"

# 潤色文稿
python3 glm_researcher.py polish --file ./my_draft.txt --style academic

# 生成參考文獻
python3 glm_researcher.py references --topic "自然語言處理" --num 10
```

---

## 📖 詳細使用指南

### 互動模式

啟動互動式TUI介面：

```bash
python3 glm_researcher.py --interactive
```

```
glmr> help
Available Commands:
  abstract    - 生成論文摘要
  intro       - 生成引言部分
  lit-review  - 生成文獻綜述
  methodology - 生成方法論
  conclusion  - 生成結論
  polish      - 潤色現有文字
  references  - 生成參考文獻
  outline     - 顯示論文大綱模板
  help        - 顯示幫助資訊
  exit        - 退出互動模式
```

### 命令詳解

#### 📝 生成摘要
```bash
python3 glm_researcher.py abstract \
  --topic "區塊鏈技術在供應鏈管理的應用" \
  --keywords "區塊鏈,供應鏈,智慧合約" \
  --methodology "實證研究"
```

#### 📚 生成引言
```bash
python3 glm_researcher.py intro \
  --topic "區塊鏈技術研究" \
  --questions "現有研究的局限性是什麼?" \
              "本研究的創新點在哪裡?" \
              "預期貢獻是什麼?"
```

#### 🔬 生成方法論
```bash
python3 glm_researcher.py methodology \
  --type quantitative \
  --subject "電腦科學"
```

### 配置管理

設定預設API密鑰：
```bash
# 臨時設定
export ZHIPU_API_KEY="your-api-key"

# 永久設定（添加到~/.bashrc或~/.zshrc）
echo 'export ZHIPU_API_KEY="your-api-key"' >> ~/.bashrc
```

### 常見問題

**Q: API密鑰無效？**
```bash
# 檢查密鑰是否正確設定
echo $ZHIPU_API_KEY

# 或直接傳入密鑰
python3 glm_researcher.py --api-key "your-key" abstract --topic "..."
```

**Q: 網路連接錯誤？**
```bash
# 檢查網路連接
ping open.bigmodel.cn

# 或設定代理
export HTTP_PROXY="http://proxy:port"
export HTTPS_PROXY="http://proxy:port"
```

---

## 💡 設計思路與迭代規劃

### 設計理念

1. **極簡主義** - 零外部依賴，降低使用門檻
2. **隱私優先** - 數據本地處理，保護學術隱私
3. **學術規範** - 嚴格遵循APA/MLA等學術寫作規範
4. **持續優化** - 基於用戶反饋不斷迭代改進

### 技術選型

| 組件 | 選型 | 原因 |
|------|------|------|
| 語言 | Python 3.8+ | 學術領域廣泛使用 |
| 模型 | GLM-5.1 | 128K超長上下文 |
| API | 智譜OpenAPI | 中國區訪問穩定 |
| 無依賴 | urllib.request | Python標準庫 |

### 後續迭代

- [ ] 📄 支援更多論文模板（IEEE、ACM、Nature等）
- [ ] 🌐 支援更多語言（中英日韓）
- [ ] 📊 添加圖表生成功能
- [ ] 🔍 整合文獻檢索API
- [ ] 📝 支援LaTeX格式導出

---

## 📦 打包與部署

### 打包為獨立可執行檔案

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

構建並執行：
```bash
docker build -t glm-researcher .
docker run -it glm-researcher
```

---

## 🤝 貢獻指南

歡迎提交Issue和Pull Request！

### 提交規範

```
feat: 新增論文模板
fix: 修復API調用問題
docs: 更新文檔
refactor: 重構代碼
test: 添加測試
```

### 開發流程

1. Fork專案
2. 建立特性分支 `git checkout -b feature/AmazingFeature`
3. 提交更改 `git commit -m 'Add some AmazingFeature'`
4. 推送到分支 `git push origin feature/AmazingFeature`
5. 建立Pull Request

---

## 📄 開源協議

本專案基於 [MIT License](LICENSE) 開源。

---

## 🙏 致謝

- [智譜AI](https://www.zhipuai.cn/) - 提供GLM-5.1大語言模型API
- 所有貢獻者和用戶

---

<p align="center">
  <strong>Made with ❤️ for researchers worldwide</strong><br>
  🔬 GLM-Researcher - 讓學術寫作更簡單
</p>
