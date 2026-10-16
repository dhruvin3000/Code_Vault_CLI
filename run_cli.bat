@echo off
chcp 65001 >nul
title Code Vault CLI

REM ── Step 1: Try portable Python bundled with the CLI ─────────────
if exist "%~dp0python_portable\python.exe" (
    "%~dp0python_portable\python.exe" "%~dp0cli.py" %*
    exit /b
)

REM ── Step 2: Try Python from system PATH ──────────────────────────
where python >nul 2>&1
if %errorlevel% equ 0 (
    python "%~dp0cli.py" %*
    exit /b
)

where python3 >nul 2>&1
if %errorlevel% equ 0 (
    python3 "%~dp0cli.py" %*
    exit /b
)

REM ── Step 3: Nothing found ────────────────────────────────────────
echo.
echo [ERROR] Python is not installed or not in PATH.
echo.
echo   Option 1: Install Python from https://www.python.org/downloads/
echo             (Check "Add Python to PATH" during installation)
echo.
echo   Option 2: Place a Python installation in:
echo             %~dp0python_portable\
echo.
pause
