# 🎯 DHRUVIN's Code Vault CLI

A powerful command-line interface to browse, explore, and **run** all your code files from one central place!

**✨ NEW: White theme with horizontal grid layout for maximum screen coverage!**  
**🔄 LIVE RESIZING: Adjusts automatically when you resize your terminal window!**

---

## 🚀 Quick Start

### Windows

**Option 1: Batch File (Recommended)**
```bash
run_cli.bat
```

**Option 2: PowerShell**
```powershell
.\run_cli.ps1
```

> **Note:** Portable Python 3.12 is included in `python_portable/` folder, so you don't need to install Python separately!

---

## ✨ Features

### � **Live Window Resizing** 🆕
- **Automatically adjusts** to terminal window size changes
- Resize your CMD/PowerShell window **anytime** - no restart needed!
- Grid columns adapt: narrow window = 1-2 columns, wide window = 3-4 columns
- Banner, breadcrumb, and navigation stay perfectly centered
- Just navigate or type a command after resizing - it adapts instantly!

### �📂 **Smart File Browser**
- Navigate through all your code folders
- Color-coded directories and files
- File type icons (Python 🐍, Java ☕, JavaScript 🟨, C ⚙️, etc.)
- Shows folder statistics (dirs/files count)
- Breadcrumb navigation

### ▶️ **Code Runner**
Run code files directly from the CLI! Supports:

| Language | Extension | Requirements |
|----------|-----------|--------------|
| **Python** | `.py` | Python 3.x |
| **C** | `.c` | GCC (MinGW) |
| **C++** | `.cpp` | G++ (MinGW) |
| **Java** | `.java` | JDK (javac + java) |
| **JavaScript** | `.js` | Node.js |
| **TypeScript** | `.ts` | ts-node or npx |
| **HTML** | `.html` | Default browser |
| **PHP** | `.php` | PHP CLI |
| **Kotlin** | `.kt` | kotlinc + JRE |
| **SQL** | `.sql` | View only (needs DB) |
| **Arduino** | `.ino` | View only (needs IDE) |
| **Jupyter** | `.ipynb` | Jupyter Notebook |

### 🌳 **Tree View**
- Visualize your project structure
- Adjustable depth (1-5 levels)
- Beautiful ASCII tree rendering

### 🔍 **File Search**
- Search by filename or extension
- Example: search for "calculator", ".py", "sort"
- Shows all matches with full path
- Run files directly from search results

### 👁️ **File Preview**
- View file contents (first 60 lines)
- Line numbers for easy reference
- Syntax highlighting hints via file icons

---

## 🎮 Navigation Commands

When browsing directories:

| Command | Action |
|---------|--------|
| `1-99` | Enter folder or open file (by number) |
| `B` | Go back to previous folder |
| `H` | Return to home (Codes root) |
| `T` | Show tree view |
| `S` | Search files |
| `Q` | Quit the CLI |

When viewing a file:

| Option | Action |
|--------|--------|
| `1` | ▶️ Run the file |
| `2` | 👁️ View contents |
| `3` | ↩️ Back |

---

## 📋 System Requirements

### Included (No Install Needed)
- ✅ Python 3.12 (portable version in `python_portable/`)

### Optional (For Code Execution)
- **C/C++**: MinGW GCC/G++ ([Download](https://sourceforge.net/projects/mingw/))
- **Java**: JDK 8+ ([Download](https://www.oracle.com/java/technologies/downloads/))
- **Node.js**: For JavaScript/TypeScript ([Download](https://nodejs.org/))
- **PHP**: PHP CLI ([Download](https://www.php.net/downloads))

> **Tip:** Add these to your system PATH for seamless execution!

---

## 🎨 Features in Detail

### Color Coding
- **Folders**: Bright cyan, green, yellow, magenta (rotating)
- **Runnable files**: Green ▶️ tag
- **File types**: Each language has its own color and icon

### Smart Compilation
- **C/C++**: Auto-compiles with GCC/G++, runs executable
- **Java**: Auto-compiles with javac, runs with java
- **Others**: Direct execution

### Error Handling
- Missing compilers/interpreters: Clear error messages with installation links
- Compilation errors: Full error output displayed
- File not found: Safe error handling

---

## 📁 Project Structure

```
D:\Codes/                             ← CLI browses this entire folder!
├── Code_Vault_CLI/                   ← CLI application lives here
│   ├── cli.py                        # Main CLI script
│   ├── system_monitor.py             # System monitoring module
│   ├── run_cli.bat                   # Launcher (run from here!)
│   ├── run_cli.ps1                   # PowerShell launcher
│   ├── python_portable/              # Portable Python 3.12
│   └── Documentation/                # All guides
│
├── Python_programs/                  ← Your code folders (all accessible!)
├── JAVA_program/
├── C_programing_Cpp/
├── Web_Pages/
├── Android_Applications/
└── ... (all your other projects)
```

**Note:** The CLI is installed in `Code_Vault_CLI`, but it browses and operates on **all** folders in `D:\Codes`!

---

## 🛠️ Customization

### Change Root Directory
Edit `cli.py` line 42:
```python
ROOT = Path("D:/Codes")  # Currently set to browse all of D:\Codes
```

**Current Setup:** CLI browses all folders in `D:\Codes`  
**To change:** Update the ROOT path to any folder you want to browse

### Add File Types
Edit the `FILE_TYPES` dictionary in `cli.py` (lines 37-59):
```python
".rs": {"icon": "🦀", "label": "Rust", "color": C.BRIGHT_RED},
```

### Ignore More Files/Folders
Edit the ignore lists in `cli.py` (lines 32-36):
```python
IGNORED_DIRS  = {".idea", ".vscode", "node_modules", ...}
IGNORED_EXT   = {".exe", ".class", ".jar", ...}
```

---

## 🐛 Troubleshooting

### Python not found
- The CLI includes portable Python in `python_portable/`
- If it's missing, download from: https://www.python.org/downloads/
- Make sure Python is in your PATH

### ANSI colors not showing
- Use Windows Terminal or PowerShell 7+
- Old CMD may not support colors properly

### Unicode characters broken
- Set console to UTF-8: `chcp 65001`
- Use a modern terminal (Windows Terminal recommended)

### Can't run C/Java files
- Install the required compiler (GCC for C, JDK for Java)
- Add to system PATH
- Restart terminal after installation

---

## 📝 Version History

### Version 1.0 (August 2026)
- ✅ File browser with color coding
- ✅ Support for 10+ programming languages
- ✅ Tree view and search functionality
- ✅ Portable Python included
- ✅ Windows batch and PowerShell launchers

---

## 👤 Author

**DHRUVIN**  
📦 Code Vault: `D:\Codes` (browsing all folders)  
🛠️ CLI Location: `D:\Codes\Code_Vault_CLI`

---

## 📜 License

Free to use and modify for personal projects!

---

## 🎉 Tips & Tricks

1. **Fast Navigation**: Use numbers instead of typing folder names
2. **Quick Search**: Press `S` from anywhere to search all files
3. **Tree Preview**: Use `T` to get a bird's-eye view before diving in
4. **Home Reset**: Press `H` if you get lost in nested folders
5. **Compile Once**: C/Java files auto-compile before running
6. **🆕 Dynamic Resize**: Resize your window anytime - CLI adapts on next screen refresh!
7. **🆕 Fullscreen Mode**: Press F11 in Windows Terminal for maximum columns!

---

## 📖 Additional Guides

- **`DYNAMIC_RESIZE_GUIDE.md`** - Learn how live window resizing works
- **`NEW_CLI_DESIGN.md`** - Details about the white theme redesign

---

**Happy Coding! 🚀**
