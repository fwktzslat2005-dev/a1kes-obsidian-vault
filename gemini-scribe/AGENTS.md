# AGENTS.md

This file provides context about this Obsidian vault for AI agents.

## Vault Overview

本知识库主要用于两个领域：一是电气工程专业的学术笔记，涵盖电力系统分析和电气设备原理；二是面向 Obsidian 的 Gemini AI 助手技能开发与管理。它既是一个结构化的学习资源库，也是一个用于配置和优化 AI 代理功能的实验平台。

## Organization

知识库采用清晰的分支结构：

- **专业知识区**：以“电气设备及主系统”和“电力系统分析”为核心，遵循教材章节结构（如第1章、第6章），按层级组织笔记，便于系统性查阅。
- **技术开发区**：以 `gemini skills/` 文件夹为核心，采用模块化管理，根据功能（如 `obsidian-markdown`, `json-canvas`, `state-grid-assistant`）对 AI 技能进行分类存储。

## Key Topics

- 电力系统分析（短路电流计算、无限大功率电源供电系统）
- 电气设备原理（发电厂类型：火电、核电、新能源）
- Obsidian 自动化与 AI 技能开发（Markdown 处理、JSON Canvas、CLI 工具）
- 国网相关业务（State Grid Assistant）

## User Preferences

用户偏好使用中文进行交流和记录。倾向于结构化、严谨的笔记风格，通常遵循教材或逻辑分类的层级。在处理 AI 指令时，用户重视模块化和可维护性。

- **语言偏好**：必须使用中文。
- **Callout 偏好**：所有 `Insert as Callout` 操作必须使用 `> [!info]-` 格式，以确保内容默认折叠。

## Custom Instructions

- **学术笔记**：在回答电气工程相关问题时，应优先引用“电力系统分析”或“电气设备及主系统”中的现有章节内容。
- **技能开发**：在编写或修改 AI 技能时，请参考 `gemini skills/` 下的现有结构，保持模块化和清晰的文档说明。
- **引用规范**：在处理相关笔记时，尽量使用 [[WikiLinks]] 进行关联，保持知识库的互联性。
