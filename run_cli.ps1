# Code Vault CLI — PowerShell Launcher
$Host.UI.RawUI.WindowTitle = "Code Vault CLI"

# Enable UTF-8 and ANSI colors
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:TERM = "xterm-256color"

$scriptPath    = Join-Path $PSScriptRoot "cli.py"
$portablePython = Join-Path $PSScriptRoot "python_portable\python.exe"

# ── Step 1: Portable Python bundled with the CLI ──────────────────
if (Test-Path $portablePython) {
    & $portablePython $scriptPath @args
    exit
}

# ── Step 2: Python from system PATH ──────────────────────────────
if (Get-Command python -ErrorAction SilentlyContinue) {
    python $scriptPath @args
    exit
}

if (Get-Command python3 -ErrorAction SilentlyContinue) {
    python3 $scriptPath @args
    exit
}

# ── Step 3: Not found ─────────────────────────────────────────────
Write-Host ""
Write-Host "[ERROR] Python not found." -ForegroundColor Red
Write-Host ""
Write-Host "  Option 1: Install Python from https://www.python.org/downloads/" -ForegroundColor Yellow
Write-Host "            (Check 'Add Python to PATH')" -ForegroundColor Yellow
Write-Host ""
Write-Host "  Option 2: Place a Python installation in:" -ForegroundColor Yellow
Write-Host "            $PSScriptRoot\python_portable\" -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to exit"
