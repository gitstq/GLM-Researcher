# 🌐 Language Switcher | 言語切替 | 语言切换

[![简体中文](https://img.shields.io/badge/-简体中文-blue?style=flat-square)](README.md)
[![English](https://img.shields.io/badge/-English-red?style=flat-square)](README_EN.md)
[![繁體中文](https://img.shields.io/badge/-繁體中文-green?style=flat-square)](README_ZH_TW.md)
[![日本語](https://img.shields.io/badge/-日本語-orange?style=flat-square)](README_JA.md)

---

# 🔬 GLM-Researcher | ローカル学術論文ライティングアシスタント

> 🚀 **ゼロ依存 · GLM-5.1搭載 · ローカル実行 · プライバシー保護**

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/yourusername/GLM-Researcher?style=flat-square)](https://github.com/yourusername/GLM-Researcher/stargazers)

---

## 🎉 プロジェクト紹介

**GLM-Researcher**は、智譜AIの **GLM-5.1** 大規模言語モデルに基づいた軽量なローカル学術論文ライティングアシスタントです。 **128Kコンテキストウィンドウ** をサポートし、超長文書を一度に処理できます。

### ✨ コアバリュー

- 🔒 **プライバシー保護** - 全データをローカル処理、クラウドにアップロード不要
- 💰 **コスト管理** - GLM-4-Flash高コストパフォーマンスモデルを使用
- 📦 **ゼロ依存** - Python標準ライブラリのみ、追加パッケージ不要
- 🎯 **学術特化** - 学術ライティングシーンに最適化

### 🆚 自社開発の差別化ポイント

| 機能 | GLM-Researcher | 他のソリューション |
|------|----------------|----------|
| 依存関係 | **ゼロ** | 複数パッケージ必要 |
| デプロイ | **ローカル** | API呼び出し/クラウド必要 |
| コンテキスト | **128K** | 通常8K-32K |
| オフライン | **完全対応** | 制限あり |
| 中国市場 | **ネイティブ対応** | 部分対応 |

---

## 🚀 クイックスタート

### 環境要件

- Python 3.8+
- 智譜AI API Key

### インストール手順

```bash
# プロジェクトをクローン
git clone https://github.com/yourusername/GLM-Researcher.git
cd GLM-Researcher

# APIキーを設定
export ZHIPU_API_KEY="your-api-key-here"

# セットアップスクリプトを実行
chmod +x setup.sh
./setup.sh
```

### クイック使用方法

```bash
# インタラクティブモード
python3 glm_researcher.py --interactive

# 要点を生成
python3 glm_researcher.py abstract --topic "AIの教育応用" \
  --keywords "機械学習,教育,人工知能"

# 論文アウトライン生成
python3 glm_researcher.py outline --type empirical

# 文献レビュー生成
python3 glm_researcher.py lit-review --topic "ディープランニング研究" \
  --themes "理論的基盤" "先行研究" "方法論" "研究の空白"

# 文章の改善
python3 glm_researcher.py polish --file ./my_draft.txt --style academic

# 参考文献生成
python3 glm_researcher.py references --topic "自然言語処理" --num 10
```

---

## 📖 詳細使用ガイド

### インタラクティブモード

インタラクティブTUIインターフェースを起動：

```bash
python3 glm_researcher.py --interactive
```

```
glmr> help
Available Commands:
  abstract    - 要点を生成
  intro       - 序論セクションを生成
  lit-review  - 文献レビューを生成
  methodology - 方法論セクションを生成
  conclusion  - 結論セクションを生成
  polish      - 既存テキストを改善
  references  - 参考文献リストを生成
  outline     - 論文アウトラインテンプレートを表示
  help        - ヘルプメッセージを表示
  exit        - インタラクティブモードを終了
```

### コマンド詳細

#### 📝 要点を生成
```bash
python3 glm_researcher.py abstract \
  --topic "サプライチェーンマネジメントにおけるブロックチェーン応用" \
  --keywords "ブロックチェーン,サプライチェーン,スマートコントラクト" \
  --methodology "実証研究"
```

#### 📚 序論を生成
```bash
python3 glm_researcher.py intro \
  --topic "ブロックチェーン技術研究" \
  --questions "既存研究の限界は何ですか？" \
              "本研究の革新点在哪里？" \
              "期待される貢献は何ですか？"
```

#### 🔬 方法論を生成
```bash
python3 glm_researcher.py methodology \
  --type quantitative \
  --subject "コンピュータサイエンス"
```

### 設定管理

デフォルトAPIキーを設定：
```bash
# 一時設定
export ZHIPU_API_KEY="your-api-key"

# 恒久設定（~/.bashrcまたは~/.zshrcに追加）
echo 'export ZHIPU_API_KEY="your-api-key"' >> ~/.bashrc
```

### よくある問題

**Q: APIキーが無効？**
```bash
# キーが正しく設定されているか確認
echo $ZHIPU_API_KEY

# または直接キーを渡す
python3 glm_researcher.py --api-key "your-key" abstract --topic "..."
```

**Q: ネットワーク接続エラー？**
```bash
# ネットワーク確認
ping open.bigmodel.cn

# またはプロキシを設定
export HTTP_PROXY="http://proxy:port"
export HTTPS_PROXY="http://proxy:port"
```

---

## 💡 設計思想とロードマップ

### 設計理念

1. **ミニマリズム** - 外部依存ゼロ、使用门槛降低
2. **プライバシー優先** - データローカル処理、学術プライバシーを保護
3. **学術規範** - APA/MLAなど学術ライティング規則を厳守
4. **継続的改善** - ユーザーフィードバックに基づく反復的改善

### 技術選定

| コンポーネント | 選定 | 理由 |
|------|------|------|
| 言語 | Python 3.8+ | 学術分野で広く使用 |
| モデル | GLM-5.1 | 128K超長コンテキスト |
| API | 智譜OpenAPI | 中国地域アクセス安定 |
| 依存なし | urllib.request | Python標準ライブラリ |

### 今後のロードマップ

- [ ] 📄 更多論文テンプレートをサポート（IEEE、ACM、Natureなど）
- [ ] 🌐 更多信息言語をサポート（中、英、日、韓）
- [ ] 📊 チャート/ダイアグラム生成機能を追加
- [ ] 🔍 文献検索APIを統合
- [ ] 📝 LaTeXエクスポートをサポート

---

## 📦 パッケージングとデプロイ

### スタンドアロン実行ファイルとしてパッケージ

PyInstallerを使用：
```bash
pip install --break-system-packages pyinstaller
pyinstaller --onefile --name GLM-Researcher glm_researcher.py
```

### Dockerデプロイ

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN chmod +x setup.sh
ENV ZHIPU_API_KEY="your-api-key"
CMD ["python3", "glm_researcher.py", "--interactive"]
```

ビルドと実行：
```bash
docker build -t glm-researcher .
docker run -it glm-researcher
```

---

## 🤝 コントリビューションガイド

IssueとPull Requestの提出を歓迎します！

### コミット規則

```
feat: 新規論文テンプレート追加
fix: API呼び出し問題の修正
docs: ドキュメント更新
refactor: コードリファクタリング
test: テスト追加
```

### 開発ワークフロー

1. プロジェクトをフォーク
2. フィーチャーブランチを作成 `git checkout -b feature/AmazingFeature`
3. 変更をコミット `git commit -m 'Add some AmazingFeature'`
4. ブランチにプッシュ `git push origin feature/AmazingFeature`
5. Pull Requestを作成

---

## 📄 オープンソースライセンス

このプロジェクトは [MIT License](LICENSE) に基づいてライセンスされています。

---

## 🙏 謝辞

- [智譜AI](https://www.zhipuai.cn/) - GLM-5.1大規模言語モデルAPIの提供
- すべての貢献者とユーザー

---

<p align="center">
  <strong>Made with ❤️ for researchers worldwide</strong><br>
  🔬 GLM-Researcher - 学術ライティングをシンプルに
</p>
