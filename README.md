# 📁 File Organizer

![Python](https://img.shields.io/badge/Python-3.13-blue)
![uv](https://img.shields.io/badge/package%20manager-uv-purple)
![Ruff](https://img.shields.io/badge/linter-Ruff-red)
![MyPy](https://img.shields.io/badge/type%20checking-MyPy-blue)
![Pytest](https://img.shields.io/badge/tests-Pytest-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)

> Production-style CLI tool for automatic file organization using YAML rules, structured logging, and Docker support.

---

## 🚀 Overview

File Organizer is a Python CLI tool that scans directories and organizes files into categorized folders based on YAML configuration.

Focus:
- automation
- reproducibility
- clean architecture
- testability

---

## ✨ Features

- File classification by extension
- YAML configuration
- Directory scanning
- Safe file moving
- Dry-run mode
- JSON reports
- Structured logging
- Typer CLI (multi-command)
- Docker support
- Pytest suite

---

## 📂 Project Structure

```text
file-organizer/
├── config/
│   └── rules.yaml
├── reports/
│   └── ...
├── src/
│   └── file_organizer/
│       ├── __init__.py
│       ├── config.py
│       ├── logging.py
│       ├── main.py
│       ├── models.py
│       ├── organizer.py
│       ├── reporter.py
│       ├── scanner.py
├── tests/
│   ├── test_cli.py
│   ├── test_config.py
│   ├── test_organizer.py
│   ├── test_reporter.py
│   └── test_scanner.py
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## 🏗 Architecture

```text
CLI (Typer)
   |
   v
Scanner
   |
   v
Organizer
   |
   v
Reporter
   |
   v
Logger

```

---

## Installation

Clone repository

```bash
git clone https://github.com/sendersk/file-organizer.git
cd file-organizer
```

Install dependencies (uv)

```bash
uv sync
```

---

# Usage

### Show help
```bash
uv run file-organizer --help
```

### Organize files
```bash
uv run file-organizer organize ./data
```

### Dry-run mode (safe simulation)
```bash
uv run file-organizer organize ./data --dry-run
```

### Version
```bash
uv run file-organizer version
```

---

# Example
Before

```text
data/
├── photo.jpg
├── document.pdf
├── video.mp4
```

After
```text
data/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── document.pdf
├── Videos/
│   └── video.mp4
└── reports/
    └── report.json
```

---

# Configuration

Example config/rules.yaml:

```text
categories:
  Images:
    - .jpg
    - .jpeg
    - .png

  Documents:
    - .pdf
    - .docx
    - .txt

  Videos:
    - .mp4
    - .mov

  Other: []
```

---

# Report

Generated JSON report:

```text
{
  "processed": 10,
  "categorized": {
    "Images": 4,
    "Documents": 3,
    "Videos": 2,
    "Other": 1
  }
}
```

---

# Logging

Console output
```text
[INFO] Starting organization process
[INFO] Processing file: photo.jpg -> Images
[INFO] Organization completed successfully

```

File logs (JSON)

Stored in:

```text
logs/app.log
```

Example:
```text
{"timestamp":"2026-01-23T12:00:00","level":"INFO","message":"Processing file photo.jpg -> Images"}
```

---

# 🐳 Docker

Build image
```bash
docker build -t file-organizer .
```

Run container
```bash
docker run --rm file-organizer organize /data
```

---

# 🐙 Docker Compose

```bash
docker compose run --rm organizer
```

---

# 🧪 Testing

Run tests:
```bash
uv run pytest
```

With coverage:
```bash
uv run pytest --cov=src
```

---

# 🧠 Design principles
- Single Responsibility Principle (SRP)
- Clear separation of layers (CLI / logic / IO)
- Pathlib-first file handling
- Testable service-based architecture
- CLI as orchestration layer only
- Safe-by-default operations (dry-run support)

---

# 🛠 Tech Stack
- Python 3.13+
- Typer (CLI framework)
- Pydantic (data validation)
- PyYAML (configuration)
- pytest (testing)
- Ruff (linting)
- MyPy (type checking)
- uv (package manager)
- Docker / Docker Compose

---

# 📌 Safety
- ```--dry-run``` prevents destructive operations
- Explicit file path validation
- Structured logging for full traceability
- Safe directory creation

---

# 🚀 Roadmap
- Watch mode (real-time file monitoring)
- Plugin system for custom rules
- Cloud storage support (S3 / GDrive)
- Scheduling / automation mode
- Web dashboard (optional UI)

---

# 👨‍💻 Author
Created by Przemysław Senderski