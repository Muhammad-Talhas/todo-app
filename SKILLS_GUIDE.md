# Creating Skills in the SDD Framework

This document explains how to create skills in this Spec-Driven Development (SDD) project.

## What are Skills?

Skills in this project are specialized command files that define structured workflows for specific development tasks. They are implemented as markdown files with YAML frontmatter that contain detailed instructions for AI agents to execute complex development processes.

## Skill File Structure

Skills are stored in the `.claude/commands/` directory and follow the naming pattern `sp.<skill-name>.md`.

Each skill file has the following structure:

```markdown
---
description: [Brief description of what the skill does]
handoffs:
  - label: [Human-readable label for handoff]
    agent: [Name of agent to handoff to]
    prompt: [Prompt to send to the handoff agent]
    send: [true/false whether to send data]
---
## User Input
```text
$ARGUMENTS
```

[Detailed workflow instructions in markdown format]
```

## How to Create a New Skill

### 1. Choose a Skill Name
- Use the `sp.` prefix followed by a descriptive name
- Keep it concise but meaningful (e.g., `sp.code-review`, `sp.database-migration`)
- Use lowercase with hyphens for multi-word names

### 2. Create the Skill File
Create a new file in `.claude/commands/` with the naming pattern `sp.<skill-name>.md`.

### 3. Define the YAML Frontmatter
Include a description and any handoffs to other agents:

```yaml
---
description: Create or update the feature specification from a natural language feature description.
handoffs:
  - label: Build Technical Plan
    agent: sp.plan
    prompt: Create a plan for the spec. I am building with...
---
```

### 4. Define the Workflow
The main content should include:

- **User Input section**: Defines how to handle user arguments (`$ARGUMENTS`)
- **Outline section**: Detailed step-by-step workflow instructions
- **Guidelines section**: Best practices and important notes
- **PHR section**: Instructions for creating Prompt History Records

### 5. Example Skill Template

```markdown
---
description: [Brief description of what the skill does]
handoffs:
  - label: [Handoff label]
    agent: [Agent name]
    prompt: [Prompt to send]
    send: true
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

[Detailed workflow steps here]

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

[PHR instructions here]
```

## Key Elements to Include

1. **Clear workflow steps**: Break down the process into logical, sequential steps
2. **Error handling**: Define what to do in case of failures
3. **Validation**: Include quality checks and validation steps
4. **Output reporting**: Specify what information to return to the user
5. **PHR creation**: Always include instructions for creating Prompt History Records

## Available Tools in Skills

Skills can reference and use various tools:
- File system operations (Read, Write, Edit, Glob, Grep)
- Git operations
- Shell commands (with proper sandboxing)
- Template files from `.specify/templates/`
- PowerShell scripts from `.specify/scripts/powershell/`

## Best Practices

1. **Be specific**: Provide detailed instructions that an AI agent can follow without ambiguity
2. **Handle errors**: Include fallback strategies and error handling
3. **Validate outputs**: Include quality checks and validation steps
4. **Maintain consistency**: Follow the same structure as existing skills
5. **Document dependencies**: Clearly state what files, templates, or scripts the skill requires
6. **Consider handoffs**: Plan for when one skill should hand off to another

## Example: Creating a Code Review Skill

To create a `sp.code-review` skill, you would:

1. Create `.claude/commands/sp.code-review.md`
2. Define the YAML frontmatter with description and handoffs
3. Include workflow steps for:
   - Reading the changed files
   - Analyzing code quality
   - Checking against coding standards
   - Generating review comments
   - Providing improvement suggestions
4. Include validation steps and error handling
5. Add PHR creation instructions

The skill would then be available as `/sp.code-review` in the CLI.