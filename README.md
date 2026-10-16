# Code Vault CLI

A terminal-based code explorer for browsing, viewing, and running code across 10+ languages — with live system monitoring built in.

## Features

- **File browser** — navigate your entire codebase from one place
- **Code runner** — execute Python, Java, JavaScript, C, C++, TypeScript, PHP, Kotlin, HTML, Jupyter
- **System monitor** — live RAM, CPU, storage, and network stats
- **Execution tracker** — CPU/RAM usage graphs and timing reports per run
- **Data flow visualizer** — step-by-step breakdown of what happens when code runs
- **Search** — find any file by name or extension across all folders
- **Tree view** — show directory structure up to 5 levels deep
- Adapts to any terminal width automatically

## Quick Start

### Option 1 — Double-click launcher (Windows)
```
run_cli.bat
```

### Option 2 — PowerShell
```powershell
.\run_cli.ps1
```

### Option 3 — Python directly
```bash
python cli.py                          # Browse current parent directory
python cli.py D:\Codes                 # Browse a specific path
python cli.py --help
```

### Option 4 — Install as a pip package
```bash
pip install -e .
codevault                              # Browse current parent directory
codevault D:\Codes                     # Browse a specific path
```

## Setting a Default Root Directory

Set the `CODEVAULT_ROOT` environment variable to avoid passing the path every time:
```bash
# Windows CMD
set CODEVAULT_ROOT=D:\Codes

# PowerShell
$env:CODEVAULT_ROOT = "D:\Codes"

# Permanent (PowerShell)
[System.Environment]::SetEnvironmentVariable("CODEVAULT_ROOT","D:\Codes","User")
```

## Installation

### Requirements
- Python 3.8+
- `psutil` (for system monitoring)

```bash
pip install -r requirements.txt
```

Or install as a package:
```bash
pip install -e .
```

A portable Python with psutil already included is in `python_portable/` — the `.bat` and `.ps1` launchers use it automatically.

## Navigation

| Key | Action |
|-----|--------|
| Number | Enter folder / open file |
| B | Go back |
| H | Home (root directory) |
| T | Tree view (choose depth 1–5) |
| S | Search files |
| M | System monitor dashboard |
| Q | Quit |

## File Actions

When you select a file:
- **Run** — compiles (if needed) and executes with live monitoring
- **View** — shows first 50 lines in the terminal
- **Back** — returns to the file list

## Supported Languages

| Language | Runner | Notes |
|----------|--------|-------|
| Python | `python` / `python3` | With execution tracking |
| Java | `javac` + `java` | Auto-compiles |
| JavaScript | `node` | With execution tracking |
| TypeScript | `ts-node` / `npx ts-node` | |
| C | `gcc` | Auto-compiles |
| C++ | `g++` | Auto-compiles |
| HTML | Default browser | Opens in browser |
| PHP | `php` | |
| Kotlin | `kotlinc` + `java -jar` | Auto-compiles |
| Jupyter | `jupyter notebook` | Opens notebook server |
| SQL | — | Shows file contents |
| Arduino `.ino` | — | Shows sketch contents |

## Project Structure

```
Code_Vault_CLI/
├── cli.py              # Main application
├── system_monitor.py   # System monitoring module
├── test_monitor.py     # Test script for monitoring
├── run_cli.bat         # Windows CMD launcher
├── run_cli.ps1         # PowerShell launcher
├── requirements.txt    # Python dependencies
├── setup.py            # Package definition
├── python_portable/    # Bundled Python (no install needed)
└── docs/               # Extended documentation
    ├── README_COMPLETE.md
    ├── SYSTEM_MONITOR_GUIDE.md
    ├── FEATURES_SUMMARY.md
    ├── WHATS_NEW.md
    └── ...
```

## License
MIT
