# 🇰🇷 每日韩语 (Korean Vocab Assistant)

> 一个轻量级、跨平台的韩语词汇学习桌面应用。采用前后端分离的单文件架构设计，支持本地数据持久化与沉浸式学习体验。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![React](https://img.shields.io/badge/React-18.2.0-61DAFB.svg)
![TailwindCSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC.svg)
![pywebview](https://img.shields.io/badge/pywebview-GUI-lightgrey.svg)

## 📖 项目简介
本项目旨在提供一个纯净、高效的韩语单词记忆工具。摒弃了繁杂的商业化功能，专注于“学习-复习-测试”的核心闭环。应用采用 `pywebview` 构建本地客户端，通过纯 JavaScript 实现了韩文发音规则的自动解析（生成罗马音），并接入有道词典 API 提供标准的原声发音。

## ✨ 核心特性
- **⚡️ 极简单机架构：** 纯本地运行，学习进度（JSON）自动序列化保存于本地，数据绝对掌握在自己手中。
- **🧠 智能复习算法：** 自动计算并生成“今日待复习”队列，提供无限强化的抽查模式。
- **📥 极速批量导入：** 支持一键读取 `.xlsx` 格式的词汇表，自动完成数据清洗、去重与韩文提取。
- **🗣️ 原声与罗马音辅助：** 内置手写的韩文拼读解析引擎，支持发音辅助与在线高清语音播报。

## 🛠️ 技术栈
- **前端:** React 18, Tailwind CSS, Babel (纯 CDN 引入，零打包配置)
- **后端:** Python 3, `pywebview`
- **数据处理:** `xlsx` (前端表格解析)

## 🚀 快速开始

### 1. 环境准备
确保你的计算机上已安装 Python 3.8 或更高版本。

### 2. 克隆仓库
```bash
git clone [https://github.com/luweiheng1688-alt/korean-vocab-assistant.git](https://github.com/luweiheng1688-alt/korean-vocab-assistant.git)
cd korean-vocab-assistant
```

### 3. 安装依赖
```bash
pip install pywebview
```

### 4. 运行应用
```bash
python main.py
```
> **注意：** 运行时请确保 `main.py` 和 `index.html` 在同一目录下。应用会在该目录自动生成 `korean_data.json` 用于保存你的学习存档。

## 📂 项目结构
```text
korean-vocab-assistant/
├── main.py            # Python 桌面端入口与本地文件读写 API
├── index.html         # 前端 UI 与核心业务逻辑 (React + Tailwind)
├── .gitignore         # Git 忽略配置（已过滤本地存档文件）
└── README.md          # 项目说明文档
```

## 🤝 参与贡献
欢迎提交 Issue 探讨新功能或反馈 Bug。如果你想添加新的特性，请提 Pull Request。
