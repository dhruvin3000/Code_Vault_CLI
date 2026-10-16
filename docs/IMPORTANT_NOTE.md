# ⚠️ IMPORTANT: How the CLI Works

## 📂 Two Different Folders

### **1. CLI Installation Folder** (Where the program lives)
```
D:\Codes\Code_Vault_CLI
```
This is where:
- ✅ `cli.py` (the program)
- ✅ `system_monitor.py` (monitoring module)
- ✅ `run_cli.bat` (launcher)
- ✅ `python_portable/` (Python interpreter)
- ✅ All documentation files

**You run the CLI from here!**

---

### **2. Browsing Root Folder** (What the CLI shows you)
```
D:\Codes
```
This is what the CLI browses and lets you access:
- 📁 Python_programs
- 📁 JAVA_program
- 📁 C_programing_Cpp
- 📁 Web_Pages
- 📁 Android_Applications
- 📁 Code_Vault_CLI (yes, itself too!)
- 📁 ... all your other project folders

**The CLI shows you all folders here!**

---

## 🎯 Quick Summary

| What | Where |
|------|-------|
| **Run CLI from** | `D:\Codes\Code_Vault_CLI\` |
| **CLI browses** | `D:\Codes\` (parent folder) |
| **You can access** | All folders in `D:\Codes` |

---

## 🚀 Example Workflow

### **Starting the CLI:**
```bash
cd D:\Codes\Code_Vault_CLI
run_cli.bat
```

### **What you'll see:**
```
            D H R U V I N
      C O D E   V A U L T   E X P L O R E R

                📦 Codes    ← You start here!
══════════════════════════════════════════════════════

📂 FOLDERS
[ 1] 📁 Android_Applications
[ 2] 📁 Arduino  
[ 3] 📁 C_programing_Cpp
[ 4] 📁 Cisco-Packetracer
[ 5] 📁 Code_Vault_CLI        ← The CLI folder itself
[ 6] 📁 cpu-scheduler-visualizer
[ 7] 📁 DBMS
[ 8] 📁 JAVA_program
[ 9] 📁 Python_programs
[10] 📁 Web_Pages
... and all your other folders!
```

---

## ✅ You Can Now:

1. ✅ Browse **all** folders in `D:\Codes`
2. ✅ Navigate into **any** project folder
3. ✅ Run **any** code file from **any** folder
4. ✅ Search across **all** your code
5. ✅ Monitor execution of **any** script

---

## 🔧 Configuration

The browsing root is set in `cli.py`:
```python
ROOT = Path("D:/Codes")
```

**To change what the CLI browses:**
1. Open `D:\Codes\Code_Vault_CLI\cli.py`
2. Find line 42
3. Change `ROOT = Path("D:/Codes")` to any folder you want

---

## 💡 Example Use Cases

### **Run a Python script from Python_programs:**
```
1. run_cli.bat
2. Type: 9 (Python_programs folder)
3. Select your script
4. Type: 1 (Run)
→ Monitors execution!
```

### **Search for a file across all folders:**
```
1. run_cli.bat
2. Press: S
3. Type: "calculator"
→ Searches in ALL folders in D:\Codes!
```

### **Navigate to Arduino project:**
```
1. run_cli.bat
2. Type: 2 (Arduino folder)
3. Browse your sketches
```

---

## 🎊 Summary

- **CLI lives in:** `Code_Vault_CLI` subfolder
- **CLI browses:** Entire `D:\Codes` folder
- **You get:** Access to all your code from one CLI!

**This is the correct setup! 🎉**

---

*Last updated: August 13, 2026*
