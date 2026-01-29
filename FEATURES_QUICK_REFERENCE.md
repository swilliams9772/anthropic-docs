# Claude Features Quick Reference
## From January 2026 Documentation (692 Pages)

---

## 🎯 Available Skills

### **Anthropic Skills** (Auto-Enabled for All Users)

| Skill | What It Does | Example Command |
|-------|-------------|-----------------|
| **Excel** | Enhanced spreadsheet creation & analysis | `claude "create a financial model with charts"` |
| **Word** | Professional document creation | `claude "create a business proposal document"` |
| **PowerPoint** | Presentation design & creation | `claude "make a 10-slide pitch deck"` |
| **PDF** | PDF document creation & formatting | `claude "create a PDF report with this data"` |

### **Partner Skills** (From Skills Directory)

| Partner | Skill | Integration |
|---------|-------|-------------|
| **Notion** | Workspace management | + MCP Connector |
| **Figma** | Design workflows | + MCP Connector |
| **Atlassian** | JIRA/Confluence | + MCP Connector |
| **BioRender** | Scientific visuals | Life Sciences |
| **Scholar Gateway** | Research databases | Academia |
| **PubMed** | Medical literature | Healthcare |
| **Benevity** | Grant management | Nonprofits |
| **Candid** | Nonprofit data | Nonprofits |
| **Chronograph** | Portfolio monitoring | Private Equity |

### **Custom Skills** (Create Your Own)

Create skills with Markdown - no coding required!

```markdown
# My Custom Skill

**Purpose**: Format Python code to company standards

**Instructions**:
1. Check for PEP 8 compliance
2. Add docstrings to all functions
3. Use company naming conventions:
   - Classes: PascalCase
   - Functions: snake_case
   - Constants: UPPER_SNAKE_CASE

**Examples**:
[Your examples here]
```

---

## 🤖 Agent SDK Built-in Tools

| Tool | Capability | Example |
|------|-----------|---------|
| **Read** | Read any file | `Read("config.json")` |
| **Write** | Create new files | `Write("output.txt", data)` |
| **Edit** | Precise edits to files | `Edit("app.py", changes)` |
| **Bash** | Run shell commands | `Bash("git status")` |
| **Glob** | Find files by pattern | `Glob("**/*.py")` |
| **Grep** | Search file contents | `Grep("TODO", "src/")` |
| **WebSearch** | Search the web | `WebSearch("AI trends 2026")` |
| **WebFetch** | Fetch web pages | `WebFetch("https://...")` |
| **AskUserQuestion** | Clarifying questions | `AskUserQuestion(options)` |

---

## 📊 Claude 4.5 Models Comparison

### **When to Use Each Model**

| Model | Best For | Speed | Cost | Context | Special Features |
|-------|----------|-------|------|---------|------------------|
| **Opus 4.5** | Maximum intelligence, critical tasks | Standard | High | 200k | ⭐ Effort Parameter<br>⭐ Computer Use Zoom |
| **Sonnet 4.5** | Agents, coding, autonomous work | Fast | Medium | 200k/1M | ⭐ Extended Autonomous Operation<br>⭐ Context Awareness<br>⭐ Parallel Tool Calls |
| **Haiku 4.5** | High-volume, real-time, subagents | Fastest | Low | 200k | ⭐ First Haiku with Extended Thinking<br>⭐ 2x faster than Sonnet 4 |

### **Model Selection Guide**

```bash
# For complex reasoning & critical analysis
claude --model opus-4-5 "analyze this security vulnerability"

# For autonomous agents & coding
claude --model sonnet-4-5 "build a REST API for user auth"

# For high-volume simple tasks
claude --model haiku-4-5 "categorize these 1000 emails"
```

---

## 🎚️ Effort Parameter (Opus 4.5 Only)

**Control token usage** vs **thoroughness**

| Level | Tokens | Use Case | Example |
|-------|--------|----------|---------|
| **Low** | ~88 | High-volume automation | "Quick summary of this file" |
| **Medium** | ~113 | Production workflows | "Review this code" |
| **High** | ~257 | Critical analysis | "Comprehensive security audit" |

**Token Savings**: 66% reduction (high → low)

```bash
# Python API example
response = client.beta.messages.create(
    model="claude-opus-4-5-20251101",
    betas=["effort-2025-11-24"],
    output_config={"effort": "medium"},
    ...
)
```

---

## 🧠 Extended Thinking

**See Claude's internal reasoning process**

| Feature | Description | Min Tokens |
|---------|-------------|------------|
| **Thinking Blocks** | Internal reasoning shown | 1024 |
| **Interleaved Thinking** | Think between tool calls | 1024 |
| **Thinking Summarization** | Condensed reasoning | 1024 |
| **Budget Control** | Limit thinking tokens | 1024-10000 |

**Available On**:
- ✅ Sonnet 3.7, 4, 4.5
- ✅ Haiku 4.5 (NEW! First Haiku)
- ✅ Opus 4, 4.1, 4.5

```bash
# Enable extended thinking
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    thinking={
        "type": "enabled",
        "budget_tokens": 2000
    },
    ...
)
```

---

## 🔧 Programmatic Tool Calling (Beta)

**50-80% efficiency gain** for multi-tool workflows

### How It Works
Instead of:
```
User → Claude → Tool 1 → Claude → Tool 2 → Claude → Result
```

You get:
```
User → Claude writes code → [Tool 1, Tool 2, Tool 3...] → Result
```

### Benefits
- ✅ Eliminates API round trips
- ✅ Filters data before context window
- ✅ Reduces latency by 50-80%
- ✅ Lower token consumption
- ✅ Conditional logic in tool execution

### Example
```python
# Query 50 regions and find top 5 - all in one API call!
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    betas=["advanced-tool-use-2025-11-20"],
    tools=[
        {"type": "code_execution_20250825", "name": "code_execution"},
        {
            "name": "query_database",
            "allowed_callers": ["code_execution_20250825"]
        }
    ],
    messages=[{"role": "user", "content": "Query all regions, find top 5"}]
)
```

---

## 💾 Memory Tool (Beta)

**Persistent storage across conversations**

### How It Works
- Claude creates/reads/updates/deletes files in `/memories` directory
- **Client-side** - you control storage
- Builds knowledge over time
- Automatic memory checking before tasks

### Use Cases
```bash
# Save project context
claude "remember this project uses TypeScript with strict mode"

# Learn from feedback
claude "save that I prefer functional programming"

# Build knowledge base
claude "store our API endpoint structure"

# Resume with context
claude --continue "what was our project setup?"
```

### Memory Operations
| Operation | Description | Example |
|-----------|-------------|---------|
| **view** | List/read memory files | `view /memories` |
| **write** | Create/update memory | `write /memories/project.xml` |
| **delete** | Remove memory | `delete /memories/old.xml` |

---

## 🌐 MCP Connectors

**Model Context Protocol** - Connect Claude to external services

### Life Sciences
- **BioRender**: Visual science communication
- **Scholar Gateway**: Research databases
- **PubMed**: Medical literature

### Nonprofits
- **Benevity**: Grant management
- **Candid**: Nonprofit data & insights

### Private Equity
- **Chronograph**: Portfolio monitoring

### Integration
```bash
# Load MCP configuration
claude --mcp-config config.json "connect to database"

# Debug MCP
claude --debug "test MCP connection"
```

---

## 🖥️ Computer Use with Zoom (Opus 4.5)

**Enhanced screen interaction**

### New Zoom Action
- Inspect specific screen regions at full resolution
- Read fine print and detailed text
- Analyze complex interfaces
- Verify precise visual details

### Use Cases
- ✅ Inspect small UI elements
- ✅ Read detailed text
- ✅ Analyze dense information
- ✅ Verify visual details before actions

---

## 📈 Context Awareness

**Models track remaining tokens in real-time**

### Available On
- ✅ Sonnet 4, 4.5
- ✅ Haiku 4.5 (NEW! First Haiku)
- ✅ Opus 4, 4.1, 4.5

### Benefits
- Prevents premature task abandonment
- Better long-running task execution
- Improved multi-window workflows
- Smarter context management

---

## 🛠️ Claude Code Commands

### Essential Commands

```bash
# Interactive mode
claude

# One-shot (non-interactive)
claude -p "your prompt"

# Continue last conversation
claude --continue

# Resume specific session
claude --resume [session-id]

# Specify model
claude --model sonnet-4-5 "your prompt"

# Control tools
claude --allowed-tools "Read,Edit,Bash" "your prompt"

# Permission modes
claude --permission-mode acceptEdits "your prompt"

# Output formats
claude -p --output-format json "your prompt"
claude -p --output-format stream-json "your prompt"

# Debug mode
claude --debug "your prompt"
claude --debug-file output.log "your prompt"

# IDE integration
claude --ide

# Session management
claude --session-id $(uuidgen) "new session"
claude --fork-session --resume

# MCP
claude --mcp-config config.json
```

---

## 📚 Documentation Navigation

### By Category

```bash
cd /Volumes/Samsung990/Downloads/anthropic-docs/anthropic_docs/anthropic_docs_md/

# Agent SDK (24 files)
ls en_agent-sdk_*

# API Reference (102 files)
ls en_api_*

# Skills
ls *skill*

# Claude 4.5 Features
ls en_about-claude_models_*

# Build Guides (44 files)
ls en_build-with-claude_*

# Tools (20 files)
ls en_agents-and-tools_*

# Test & Evaluate (11 files)
ls en_test-and-evaluate_*

# Support Articles (344 files)
ls en_articles_*

# Collections
ls en_collections_*

# Resources (69 files)
ls en_resources_*
```

### Quick Searches

```bash
# Find specific topics
grep -l "programmatic tool" *.md

# Search for features
grep -l "extended thinking" *.md

# Find API docs
grep -l "POST /v1/" *.md

# Locate examples
grep -l "```python" *.md
```

---

## 🎯 Common Workflows

### 1. **Build an Autonomous Agent**

```bash
claude --model sonnet-4-5 \
  --allowed-tools "Read,Edit,Bash,WebSearch" \
  "Create an agent that:
  1. Monitors GitHub for new issues
  2. Analyzes issue content
  3. Suggests labels and assignees
  4. Creates draft responses"
```

### 2. **Code Review Agent**

```bash
claude --model sonnet-4-5 \
  --allowed-tools "Read,Grep,Glob" \
  "Review all Python files:
  - Check for security issues
  - Find code smells
  - Suggest improvements
  - Generate report"
```

### 3. **Documentation Generator**

```bash
claude --model sonnet-4-5 \
  --allowed-tools "Read,Write,Glob" \
  "Generate API documentation:
  - Read all route handlers
  - Extract endpoint info
  - Create OpenAPI spec
  - Write docs/api.md"
```

### 4. **Data Analysis Workflow**

```bash
claude --model opus-4-5 \
  --output-config='{"effort": "high"}' \
  "Analyze page_metadata.json:
  - Find patterns
  - Generate insights
  - Create visualizations
  - Write executive summary"
```

### 5. **Research & Summarization**

```bash
claude --model sonnet-4-5 \
  --allowed-tools "WebSearch,WebFetch,Write" \
  "Research AI agent frameworks:
  - Search for top frameworks
  - Compare features
  - Analyze pros/cons
  - Create comparison doc"
```

---

## 💡 Pro Tips

### Efficiency
1. ✅ Use **Haiku 4.5** for simple tasks (when available)
2. ✅ Use **Sonnet 4.5** for agents & complex coding
3. ✅ Use **Opus 4.5** with effort parameter for cost control
4. ✅ Enable **extended thinking** for transparent reasoning
5. ✅ Use **programmatic tool calling** for multi-tool workflows

### Cost Optimization
1. ✅ Start with **low effort** for simple tasks
2. ✅ Use **medium effort** for production
3. ✅ Reserve **high effort** for critical analysis
4. ✅ Use **Haiku 4.5** for high-volume operations
5. ✅ Enable **prompt caching** for repeated contexts

### Debugging
1. ✅ Use `--debug` flag for troubleshooting
2. ✅ Use `--debug-file` to save logs
3. ✅ Enable **extended thinking** to see reasoning
4. ✅ Check **context awareness** for token usage
5. ✅ Review session history with `--resume`

---

## 📖 Learning Path

### **Beginner** (Week 1)
1. ✅ Install & authenticate Claude Code
2. ✅ Try basic commands with `-p` flag
3. ✅ Explore Anthropic Skills (Excel, Word, PowerPoint)
4. ✅ Read Agent SDK overview
5. ✅ Test with simple file operations

### **Intermediate** (Week 2)
1. ✅ Build first autonomous agent
2. ✅ Create custom skill
3. ✅ Use extended thinking
4. ✅ Test different models (Opus, Sonnet, Haiku)
5. ✅ Experiment with tool combinations

### **Advanced** (Week 3)
1. ✅ Implement programmatic tool calling
2. ✅ Set up MCP connectors
3. ✅ Use memory tool for persistent context
4. ✅ Build multi-agent systems
5. ✅ Deploy production workflows

---

## 🔗 Quick Links

- **Full Analysis**: `DOCUMENTATION_UPDATES_ANALYSIS.md`
- **Top 10 Updates**: `TOP_10_UPDATES.md`
- **What's New Summary**: `WHATS_NEW_SUMMARY.txt`
- **Test Results**: `TEST_RESULTS.md`
- **Setup Guide**: `CLAUDE_CODE_SETUP_GUIDE.md`

---

**Everything you need to master Claude 4.5 and build autonomous AI agents!** 🚀
