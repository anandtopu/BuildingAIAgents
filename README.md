# Building AI Agents with LangChain and LangGraph

Build intelligent agentic systems by combining prompts, LLMs, and tools for reasoning and action. This project is part of a course focused on practical LangChain agent development, custom tool integration, and workflow design with LangGraph.

## Project Overview

Every day, intelligent systems are transforming industries through automated support, personalized recommendations, and dynamic data processing. Agentic workflows are at the core of that shift.

In this repository, you will learn how to:

- Set up and run a ReAct-style agent with OpenAI.
- Build and register custom tools using LangChain's `@tool` decorator.
- Integrate natural-language queries with tools for real-world math tasks.
- Understand how LangGraph structures workflows using graphs, nodes, and edges.

## Learning Path

- **Module 1**: Agent fundamentals, ReAct pattern, and first agent invocation.
- **Module 2**: Custom tool creation and tool-driven query workflows.

## Project Structure

```text
BuildingAIAgents/
|-- Instructions_Module1.md
|-- Instructions_Module2.md
|-- requirements.txt
|-- README.md
|-- Exercises/
|   |-- CreateAReActAgent.py
|   |-- CreateToolForMathCalculatins.py
|   `-- Integratingcustomtoolsandqueries.py
`-- Slides/
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Set your OpenAI API key.

### Quick Start (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:OPENAI_API_KEY="your_api_key_here"
```

## Run Exercises

Run each exercise script as you progress through the modules:

```powershell
python .\Exercises\CreateAReActAgent.py
python .\Exercises\CreateToolForMathCalculatins.py
python .\Exercises\Integratingcustomtoolsandqueries.py
```

## Notes

- Recommended Python version: **3.10+**.
- Some exercise files are intentionally scaffolded with blanks for practice.
- If an import is missing in an exercise, follow the module instructions and add the required import from LangChain/LangGraph.

