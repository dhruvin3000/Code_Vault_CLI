@echo off
chcp 65001 >nul
title DHRUVIN's Code Vault CLI - Quick Demo

echo.
echo ═══════════════════════════════════════════════════════════
echo   DHRUVIN's Code Vault CLI - Quick Demo
echo ═══════════════════════════════════════════════════════════
echo.
echo This will demonstrate the new monitoring features!
echo.
pause

echo.
echo [Step 1] Testing system monitor module...
echo.
.\python_portable\python.exe -c "import system_monitor as sm; ram = sm.get_ram_usage(); cpu = sm.get_cpu_usage(); storage = sm.get_storage_usage(); print(f'✓ RAM: {ram[\"percent\"]:.1f}%%'); print(f'✓ CPU: {cpu[\"percent\"]:.1f}%%'); print(f'✓ Storage: {storage[\"percent\"]:.1f}%%'); print(); print('✓ System Monitor Works!')"
echo.
pause

echo.
echo [Step 2] Testing data flow visualization...
echo.
.\python_portable\python.exe -c "import system_monitor as sm; sm.visualize_data_flow('Demo Operation', ['Step 1: Load data', 'Step 2: Process', 'Step 3: Output'])"
echo.
pause

echo.
echo [Step 3] Running test script with monitoring...
echo.
.\python_portable\python.exe test_monitor.py
echo.
pause

echo.
echo ═══════════════════════════════════════════════════════════
echo   Demo Complete! Now try the full CLI:
echo.
echo   run_cli.bat
echo.
echo   Then press [M] to see the full dashboard!
echo ═══════════════════════════════════════════════════════════
echo.
pause
