---
title: Hermes Agent vs OpenClaw 横纵分析法深度研究报告
date: 2026-04-14
tag: AI Agent,开源,横纵分析
excerpt: 两者都是开源自托管的AI助手，但在核心理念上分属两个不同的产品哲学极端——Hermes是"围绕学习代理构建网关"的agent-first系统，OpenClaw是"围绕消息网关构建代理"的gateway-first助手平台。
---

# Hermes Agent vs OpenClaw 横纵分析法深度研究报告

研究时间：2026年4月14日 | 研究对象类型：AI Agent 产品 | 所属领域：开源 AI Agent

---

## 一、一句话定义

**Hermes Agent** 是由 Nous Research 构建的「围绕学习代理构建网关」的 agent-first 系统，强调越用越聪明的内置学习循环；**OpenClaw** 是「围绕消息网关构建代理」的 gateway-first 助手平台，强调统一的渠道管理和长期在线的助手基础设施。两者都是开源自托管的 AI 助手，但在核心理念上分属两个不同的产品哲学极端。

---

## 二、纵向分析：从诞生到当下

### 2.1 Hermes Agent 的起源与发展

Hermes Agent 由 **Nous Research** 开发，这是一个专注于大型语言模型和 AI Agent 技术的实验室。Hermes Agent 最早出现在 2025 年底至 2026 年初，在 2026 年 2 月左右正式发布，引起开源社区的广泛关注。

**核心定位的形成**

Hermes Agent 从一开始就被定义为「An agent that grows with you」——一个越用越聪明的自主 Agent。这个定位直接来自其核心技术创新：内置学习循环（built-in learning loop）。 Unlike traditional AI assistants that reset between sessions, Hermes Agent 能够：

- 从完成的任务中自动创建可复用的 skills  
- 在使用过程中持续优化这些 skills  
- 主动提醒自己保存重要知识到长期记忆  
- 跨会话搜索历史对话，用 LLM 总结形成对用户的深度理解

**版本迭代时间线**

从 GitHub Release Notes 可以看到清晰的版本演进：

- **v0.2.0 (2025年2月)**: 基础架构完成，开始支持多平台消息集成  
- **v0.3.0 (2026年3月17日)**: Skills 系统成熟，支持 skills 市场  
- **v0.4.0 (2026年3月)**: MCP 集成增强，安全加固  
- **v0.5.0 (2026年3月28日)**: 安全性大幅提升，容器硬化加固  
- **v0.6.0 (2026年3月30日)**: 性能优化，多后端支持完善  
- **v0.7.0 (2026年4月3日)**: 语音功能增强  
- **v0.8.0 (2026年4月)**: 浏览器自动化栈扩展  
- **v0.9.0 (2026年4月13日)**: 最新版本，80.3k stars，10.8k forks

**关键决策逻辑**

Hermes Agent 的发展轨迹有几个关键决策：

1. **选择 agent-first 而非 gateway-first**: 团队选择将 Agent 能力作为核心，Gateway 只是 Agent 的「出口」。这决定了后续所有功能都围绕 Agent 的自主性和成长性展开。  
   
2. **多执行后端策略**: 从一开始支持 local、Docker、SSH，逐步扩展到 Daytona、Singularity、Modal。这反映了「Agent 应该在任何环境运行」的理念。  

3. **开放 skills 生态**: 允许用户创建、分享、安装 skills，使得 Agent 能力可以扩展。这与「越用越聪明」的定位一致——用户可以通过 skills 让 Agent 学到新能力。  

4. **OpenClaw 迁移工具**: 2026年初推出 `hermes claw migrate` 功能，自动导入 OpenClaw 的配置、记忆、skills、API keys。这是对竞品的直接「收割」策略。

### 2.2 OpenClaw 的起源与发展

OpenClaw 的故事更具戏剧性。

**诞生：周末实验**

2025年11月，奥地利开发者、PSPDFKit 创始人 **Peter Steinberger** 在一个周末启动了最初的项目。这是一个实验性质的个人助手，最初名为 **Clawd**，后来因为与 Claude 的品牌混淆问题更名为 **Moltbot**，助手被称为 **Molty**。

项目迅速获得关注，名字最终确定为 **OpenClaw**。

**爆发式增长**

OpenClaw 的增长堪称奇迹：

- 2025年11-12月：从 0 到 100,000+ stars  
- 2026年1月：达到 200,000+ stars  
- 2026年2月：达到 335,000 stars，60天内超越 React 10年记录的 GitHub 最快增长项目

这个「*space lobster*」形象的海报成为 AI Agent 领域的标志性符号。

**关键节点**

- **2025年11月**: 项目启动，最初形态是一个简单的 Telegram bot  
- **2025年12月**: 添加多平台支持（Discord、Slack、WhatsApp）  
- **2026年1月**: 引入 Workspace 概念，支持多用户多工作区  
- **2026年2月**: Peter Steinberger 宣布加入 OpenAI，项目继续由开源基金会维护  
- **2026年2月**: 引入 Chrome MCP，支持挂载用户登录态的浏览器  
- **2026年3月**: 继续迭代，增强安全性和企业级功能

**Moltbook 愿景**

在核心项目之外，团队提出了 **Moltbook** 概念——一个 AI Agent 之间的社交网络，让不同 Agent 可以相互通信和协调。这反映了更宏大的愿景：不仅仅是工具，而是一个 Agent 生态系统。

### 2.3 两者的交汇与竞争

随着两者功能重叠越来越多，2026年初形成了直接竞争态势：

1. **功能趋同**: 两者都支持跨平台消息、持久记忆、定时任务、浏览器自动化、多 Agent 工作流  
   
2. **Hermes 的「收割」策略**: 推出自动迁移工具，承认 OpenClaw 用户的迁移成本极低  
   
3. **市场定位分化**: Hermes 强调「Agent 越用越聪明」，OpenClaw 强调「稳定在线的助手基础设施」

---

## 三、横向分析：竞争图谱

### 3.1 竞品场景判断

这是 **场景 B：少量竞品（2个）** 的分析。两者是一对一的直接竞争关系，没有第三极。

### 3.2 核心差异对比

| 维度 | Hermes Agent | OpenClaw |
| :---- | :---- | :---- |
| **核心理念** | Agent-first | Gateway-first |
| **架构中心** | 学习代理，越用越聪明 | 单一 Gateway 进程 |
| **记忆系统** | MEMORY.md + USER.md + FTS5 + Honcho | MEMORY.md + memory/YYYY-MM-DD.md |
| **学习机制** | 内置学习循环，自动创建/优化 skills | 手动管理 skills，偏 workspace 集成 |
| **执行后端** | 6种: local/Docker/SSH/Daytona/Singularity/Modal | 3种: Docker/SSH/OpenShell |
| **浏览器栈** | Browserbase/Browser Use/Firecrawl/Camofox/CDP/agent-browser | 隔离浏览器 + Chrome MCP |
| **多 Agent** | 子代理委托，隔离会话和终端 | 多 Agent 路由，Workspace 隔离 |
| **目标用户** | 追求 Agent 成长性的开发者 | 追求稳定在线的团队/个人 |
| **部署成本** | $5 VPS 或 serverless | 自托管，资源要求相近 |
| **最新版本** | v0.9.0 (2026.4.13) | 持续活跃开发 |

### 3.3 架构本质差异

**Hermes Agent = 以 Agent 为中心构建 Runtime**

在 Hermes 的架构中，Agent 是「大脑」，Gateway 是「嘴巴」。Agent 可以独立运行、创建 skills、调用工具、委托子任务，Gateway 只是 Agent 与用户交互的渠道之一。CLI、编辑器（ACP）、消息平台都是 Agent 的「出口」。

**OpenClaw = 以 Gateway 为中心构建 Platform**

在 OpenClaw 的架构中，Gateway 是「大脑」，Agent 是「手脚」。Gateway 是单一真相来源，管理所有会话、路由、渠道、自动化。Agent 在 Gateway 的管控下执行任务，Skills 和工具是 Gateway 模型的扩展。

### 3.4 用户视角对比

**选择 Hermes 的理由**：

- 想要一个「越用越聪明」的 Agent  
- 需要多种执行后端（本地/云/Serverless）  
- 追求 CLI 和编辑器的深度集成  
- 对 subagent 委托和复杂工作流有需求  
- 希望 Agent 能自动发现和安装新 skills

**选择 OpenClaw 的理由**：

- 想要稳定在线的多渠道助手  
- 重视工���区隔离和团队协作  
- 需要统一的渠道管理和路由  
- 偏好 Gateway 原生的自动化  
- 需要 Chrome MCP 挂载用户登录态

### 3.5 市场格局

截至 2026年4月：

- **Hermes Agent**: 80.3k stars，10.8k forks，活跃开发中  
- **OpenClaw**: 335k+ stars（GitHub 第一），成熟开源项目

两者都在快速增长，功能持续趋同，但核心理念差异保持稳定。

---

## 四、横纵交汇洞察

### 4.1 历史如何塑造了当下的竞争位置

**Hermes 的起源决定了今天的「进攻性」**

Hermes 诞生于「Agent 应该能自我进化」这个技术理想。这决定了它必须：

- 把 skill 创建和优化做成自动化  
- 用 FTS5 + LLM 实现跨会话记忆  
- 支持多种执行后端让 Agent 可以在任何环境运行  
- 最后发现需要一个 Gateway 来连接用户——但 Gateway 是配角

**OpenClaw 的起源决定了今天的「防守性」**

OpenClaw 诞生于「统一多渠道消息」这个产品需求。这决定了它必须：

- 把 Gateway 做成单一真相来源  
- 用 Workspace 概念管理多用户多场景  
- 把 Agent 作为 Gateway 的扩展能力  
- 功能围绕「助手」而非「runtime」展开

### 4.2 核心洞察

**本质区别：谁是谁的附属品？**

- Hermes: Agent 是主体，Gateway 是附件  
- OpenClaw: Gateway 是主体，Agent 是附件

这不是功能多少的问题，而是「中心在哪里」的问题。

**选择逻辑**

- 要 Agent 越用越聪明 → Hermes  
- 要多渠道稳定在线 → OpenClaw  
- 要深度 CLI/编辑器集成 → Hermes  
- 要强团队协作/工作区 → OpenClaw

### 4.3 未来推演

**最可能：功能继续趋同，理念持续分化**

两者会互相借鉴功能（Hermes 会强化渠道管理，OpenClaw 会强化学习能力），但核心理念不会改变。用户会根据自己的优先级选择。

**最危险：Hermes 吃掉 OpenClaw 市场**

Hermes 的迁移工具已经就绪，OpenClaw 用户可以零成本迁移。如果 Hermes 在「助手」体验上持续改进，可能吸引大量 OpenClaw 用户。

**最乐观：各自深化差异化定位**

Hermes 朝着「个人 AI runtime」方向深化，OpenClaw 朝着「企业助手平台」方向深化，服务不同市场需求。

---

## 五、信息来源

### 主要来源

1. **Hermes Agent 官网**: [https://hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com) ⭐⭐⭐  
2. **Hermes Agent GitHub**: [https://github.com/nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) ⭐⭐⭐ (80.3k stars)  
3. **screenshotone 博客**: [https://screenshotone.com/blog/hermes-agent-versus-openclaw/](https://screenshotone.com/blog/hermes-agent-versus-openclaw/) ⭐⭐  
4. **OpenClaw Wikipedia**: [https://en.wikipedia.org/wiki/OpenClaw](https://en.wikipedia.org/wiki/OpenClaw) ⭐⭐  
5. **Taskade 博客**: [https://www.taskade.com/blog/moltbook-clawdbot-openclaw-history](https://www.taskade.com/blog/moltbook-clawdbot-openclaw-history) ⭐⭐