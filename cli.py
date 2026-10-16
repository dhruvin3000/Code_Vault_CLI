"""
╔══════════════════════════════════════════════════════════╗
║         DHRUVIN'S CODE VAULT  —  CLI Explorer            ║
║         Browse & Run all your code from one place        ║
╚══════════════════════════════════════════════════════════╝
"""

import os
import sys
import argparse
import subprocess
import platform
import webbrowser
import shutil
import time
from pathlib import Path

# Import system monitor (with fallback if psutil not available)
try:
    import system_monitor as sysmon
    MONITOR_AVAILABLE = True
except ImportError:
    MONITOR_AVAILABLE = False

# Fix Windows console encoding
if platform.system() == "Windows":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except:
        pass

# ─────────────────────────── ANSI Colors ───────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    WHITE   = "\033[97m"
    GRAY    = "\033[37m"
    BG_WHITE = "\033[107m"
    BLACK   = "\033[30m"

def enable_ansi():
    """Enable ANSI escape codes on Windows."""
    if platform.system() == "Windows":
        os.system("")   # triggers VT100 mode in conhost/WT

enable_ansi()

# ─────────────────────────── Constants ─────────────────────────────
def _resolve_root() -> Path:
    """Resolve the root directory from CLI args, env var, or default."""
    parser = argparse.ArgumentParser(
        prog="codevault",
        description="Code Vault CLI — Browse, view, and run code from your terminal",
        add_help=True,
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Root directory to browse (default: CODEVAULT_ROOT env var, or current directory)",
    )
    parser.add_argument(
        "--version", action="version", version="Code Vault CLI v3.0.0"
    )
    args, _ = parser.parse_known_args()

    if args.path:
        root = Path(args.path).resolve()
    elif os.environ.get("CODEVAULT_ROOT"):
        root = Path(os.environ["CODEVAULT_ROOT"]).resolve()
    else:
        # Fallback: directory of the script itself (works when run from D:\Codes\projects\Code_Vault_CLI)
        root = Path(__file__).parent.parent.resolve()  # goes up to D:\Codes\projects, then one more
        # If that doesn't exist as a meaningful root, use cwd
        if not root.exists():
            root = Path.cwd()

    if not root.exists():
        print(f"[Error] Root path does not exist: {root}")
        sys.exit(1)

    return root

ROOT = _resolve_root()

IGNORED_DIRS  = {".idea", ".vscode", ".gradle", "__pycache__", "venv",
                 "node_modules", "build", "mingw64", ".git", "wrapper", "n8n"}
IGNORED_FILES = {"desktop.ini", "thumbs.db", ".gitignore", ".env.example",
                 "gradlew", "gradlew.bat"}
IGNORED_EXT   = {".exe", ".class", ".jar", ".o", ".pyc", ".lock",
                 ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf",
                 ".docx", ".npy", ".ini", ".jar", ".pka", ".pkt",
                 ".properties", ".toml", ".gradle", ".zip"}

# ────────────────── File-type metadata ─────────────────────────────
FILE_TYPES = {
    ".py":    {"icon": "🐍", "label": "Python"},
    ".java":  {"icon": "☕", "label": "Java"},
    ".c":     {"icon": "⚙️ ", "label": "C"},
    ".cpp":   {"icon": "⚙️ ", "label": "C++"},
    ".js":    {"icon": "🟨", "label": "JavaScript"},
    ".html":  {"icon": "🌐", "label": "HTML"},
    ".css":   {"icon": "🎨", "label": "CSS"},
    ".sql":   {"icon": "🗄️ ", "label": "SQL"},
    ".ino":   {"icon": "🔌", "label": "Arduino"},
    ".json":  {"icon": "📋", "label": "JSON"},
    ".md":    {"icon": "📝", "label": "Markdown"},
    ".txt":   {"icon": "📄", "label": "Text"},
    ".php":   {"icon": "🐘", "label": "PHP"},
    ".ipynb": {"icon": "📓", "label": "Jupyter"},
    ".ts":    {"icon": "🔷", "label": "TypeScript"},
    ".jsx":   {"icon": "⚛️ ", "label": "React JSX"},
    ".tsx":   {"icon": "⚛️ ", "label": "React TSX"},
    ".sh":    {"icon": "💲", "label": "Shell"},
    ".bat":   {"icon": "🪟", "label": "Batch"},
    ".kt":    {"icon": "🟣", "label": "Kotlin"},
}

# ──────────────────────── Helpers ──────────────────────────────────
def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

def pause(msg="Press Enter to continue..."):
    input(f"\n{C.WHITE}{msg}{C.RESET}")

def get_terminal_size():
    """Get terminal size (width, height), with defaults if can't detect."""
    try:
        size = shutil.get_terminal_size()
        return size.columns, size.lines
    except:
        return 120, 30

def get_terminal_width():
    """Get terminal width, default to 120 if can't detect."""
    return get_terminal_size()[0]

def get_terminal_height():
    """Get terminal height, default to 30 if can't detect."""
    return get_terminal_size()[1]

def file_info(path: Path):
    ext  = path.suffix.lower()
    meta = FILE_TYPES.get(ext, {"icon": "📁", "label": ext.lstrip(".").upper() or "File"})
    return meta

def is_runnable(path: Path) -> bool:
    return path.suffix.lower() in {".py", ".java", ".c", ".cpp", ".js", ".html", ".sql", ".ino", ".ipynb", ".php", ".ts", ".kt"}

def tool_exists(tool: str) -> bool:
    return shutil.which(tool) is not None

def count_items(folder: Path):
    dirs  = sum(1 for x in folder.iterdir() if x.is_dir()  and x.name not in IGNORED_DIRS)
    files = sum(1 for x in folder.iterdir() if x.is_file() and x.suffix.lower() not in IGNORED_EXT and x.name not in IGNORED_FILES)
    return dirs, files

# ──────────────────────── Banner ───────────────────────────────────
def print_banner():
    """Print banner - dynamically centers based on current terminal width."""
    width = get_terminal_width()  # Get width FRESH each time
    
    # ASCII art for DHRUVIN
    banner_lines = [
        "██████╗ ██╗  ██╗██████╗ ██╗   ██╗██╗   ██╗██╗███╗   ██╗",
        "██╔══██╗██║  ██║██╔══██╗██║   ██║██║   ██║██║████╗  ██║",
        "██║  ██║███████║██████╔╝██║   ██║██║   ██║██║██╔██╗ ██║",
        "██║  ██║██╔══██║██╔══██╗██║   ██║╚██╗ ██╔╝██║██║╚██╗██║",
        "██████╔╝██║  ██║██║  ██║╚██████╔╝ ╚████╔╝ ██║██║ ╚████║",
        "╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝  ╚═══╝"
    ]
    
    subtitle = "C O D E   V A U L T   E X P L O R E R"
    tagline = "Browse · Explore · Execute"
    
    print()
    # Center the banner - recalculates padding each time based on current width
    for line in banner_lines:
        padding = max(0, (width - len(line)) // 2)
        print(" " * padding + f"{C.WHITE}{C.BOLD}{line}{C.RESET}")
    
    # Center subtitle
    padding = max(0, (width - len(subtitle)) // 2)
    print(" " * padding + f"{C.WHITE}{subtitle}{C.RESET}")
    
    # Center tagline
    padding = max(0, (width - len(tagline)) // 2)
    print(" " * padding + f"{C.GRAY}{tagline}{C.RESET}")
    print()

def print_separator(width=None):
    """Print a white separator line - auto-adjusts to current terminal width."""
    if width is None:
        width = get_terminal_width()  # Get FRESH width each call
    print(f"{C.WHITE}{'═' * width}{C.RESET}")

# ──────────────────────── Grid Layout ────────────────────────────
def display_items_grid(items, item_type="folder"):
    """Display items in horizontal grid layout - dynamically adjusts to terminal width."""
    width = get_terminal_width()  # Get FRESH width for dynamic adjustment
    
    # Calculate grid dimensions - handle both strings and Path objects
    max_name_len = 20
    for item, _ in items:
        name_str = str(item.name) if isinstance(item, Path) else str(item)
        max_name_len = max(max_name_len, len(name_str))
    
    card_width = min(max_name_len + 15, 35)  # Icon + number + name + padding
    cols = max(width // card_width, 1)  # Recalculate columns based on current width
    
    print_separator()
    
    if item_type == "folder":
        print(f"  {C.WHITE}{C.BOLD}📂 FOLDERS{C.RESET}")
    else:
        print(f"  {C.WHITE}{C.BOLD}📄 FILES{C.RESET}")
    
    print()
    
    # Display in grid
    for i in range(0, len(items), cols):
        row_items = items[i:i+cols]
        
        # Build the row
        row_parts = []
        for item, idx in row_items:
            # Convert to string if it's a Path object
            name_str = str(item.name) if isinstance(item, Path) else str(item)
            display_name = name_str if len(name_str) <= (card_width - 10) else name_str[:(card_width - 13)] + "..."
            
            if item_type == "folder":
                cell = f"{C.WHITE}[{idx:>2}] 📁 {display_name}{C.RESET}"
            else:
                meta = file_info(item) if isinstance(item, Path) else {"icon": "📄"}
                runnable = " ▶" if isinstance(item, Path) and is_runnable(item) else ""
                cell = f"{C.WHITE}[{idx:>2}] {meta['icon']}  {display_name}{runnable}{C.RESET}"
            
            row_parts.append(cell.ljust(card_width + 20))  # +20 for ANSI codes
        
        print("  " + "".join(row_parts))
    
    print()

# ──────────────────────── Directory Listing ────────────────────────
def list_directory_view(current: Path, history: list):
    clear()
    print_banner()

    # ── Breadcrumb ── (recalculates centering based on current terminal width)
    crumb_parts = []
    tmp = current
    while tmp != ROOT and tmp.parent != tmp:
        crumb_parts.insert(0, tmp.name)
        tmp = tmp.parent
    crumb_parts.insert(0, "📦 Codes")

    if current == ROOT:
        crumb_parts = ["📦 Codes"]

    width = get_terminal_width()  # Get FRESH width for centering
    breadcrumb = "  ▸  ".join(crumb_parts)
    padding = max(0, (width - len(breadcrumb)) // 2)
    print(" " * padding + f"{C.WHITE}{C.BOLD}{breadcrumb}{C.RESET}")
    print()

    # ── Collect items ──
    try:
        all_items = sorted(current.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        print(f"  {C.WHITE}⛔ Permission denied.{C.RESET}")
        pause()
        return None

    dirs  = [x for x in all_items if x.is_dir()  and x.name not in IGNORED_DIRS]
    files = [x for x in all_items if x.is_file() and x.suffix.lower() not in IGNORED_EXT and x.name not in IGNORED_FILES]

    entries = []

    # ── Display Folders in Grid ──
    if dirs:
        folder_items = []
        for i, d in enumerate(dirs):
            idx = len(entries) + 1
            entries.append((d, "dir"))
            try:
                dc, fc = count_items(d)
                name_with_info = f"{d.name} ({dc}d, {fc}f)"
            except:
                name_with_info = d.name
            folder_items.append((name_with_info, idx))
        
        display_items_grid(folder_items, "folder")

    # ── Display Files in Grid ──
    if files:
        file_items = []
        for f in files:
            idx = len(entries) + 1
            entries.append((f, "file"))
            file_items.append((f, idx))
        
        display_items_grid(file_items, "file")

    if not dirs and not files:
        print(f"  {C.GRAY}(empty directory){C.RESET}\n")

    # ── Navigation options ── (recalculates centering dynamically)
    print_separator()
    nav = []
    if history:
        nav.append(f"{C.WHITE}[B]{C.RESET} ← Back")
    if current != ROOT:
        nav.append(f"{C.WHITE}[H]{C.RESET} 🏠 Home")
    nav.append(f"{C.WHITE}[T]{C.RESET} 🌳 Tree")
    nav.append(f"{C.WHITE}[S]{C.RESET} 🔍 Search")
    if MONITOR_AVAILABLE:
        nav.append(f"{C.WHITE}[M]{C.RESET} ⚡ Monitor")
    nav.append(f"{C.WHITE}[Q]{C.RESET} Quit")
    
    width = get_terminal_width()  # Get FRESH width for centering navigation
    nav_str = "    ".join(nav)
    padding = max(0, (width - len(nav_str) + 40) // 2)  # +40 for ANSI codes
    print(" " * padding + nav_str)
    print_separator()

    choice = input(f"\n  {C.WHITE}{C.BOLD}→ Enter command: {C.RESET}").strip().lower()

    if choice == "q":
        return "quit"
    elif choice == "b" and history:
        return "back"
    elif choice in ("h", "home"):
        return "home"
    elif choice == "t":
        return "tree"
    elif choice == "s":
        return "search"
    elif choice == "m":
        return "monitor"
    elif choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(entries):
            path, kind = entries[idx]
            if kind == "dir":
                return ("enter", path)
            else:
                return ("file", path)
        else:
            print(f"\n  {C.WHITE}Invalid number.{C.RESET}")
            pause()
            return None
    else:
        print(f"\n  {C.WHITE}Unknown command '{choice}'.{C.RESET}")
        pause()
        return None

# ──────────────────────── Tree View ────────────────────────────────
def tree_view(root: Path, prefix="", depth=0, max_depth=3):
    if depth == 0:
        clear()
        print_banner()
        
        width = get_terminal_width()
        title = f"🌳 Tree View — {root.name}"
        padding = max(0, (width - len(title)) // 2)
        print(" " * padding + f"  {C.WHITE}{C.BOLD}{title}{C.RESET}")
        print_separator()
        print()

    if depth >= max_depth:
        return

    try:
        items = sorted(root.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except:
        return

    dirs  = [x for x in items if x.is_dir()  and x.name not in IGNORED_DIRS]
    files = [x for x in items if x.is_file() and x.suffix.lower() not in IGNORED_EXT and x.name not in IGNORED_FILES]
    all_show = dirs + files

    for i, item in enumerate(all_show):
        is_last   = (i == len(all_show) - 1)
        connector = "└── " if is_last else "├── "
        new_prefix = prefix + ("    " if is_last else "│   ")

        if item.is_dir():
            print(f"  {C.GRAY}{prefix}{connector}{C.RESET}{C.WHITE}{C.BOLD}📁 {item.name}/{C.RESET}")
            tree_view(item, new_prefix, depth + 1, max_depth)
        else:
            meta = file_info(item)
            run_tag = f" {C.WHITE}▶{C.RESET}" if is_runnable(item) else ""
            print(f"  {C.GRAY}{prefix}{connector}{C.RESET}{C.WHITE}{meta['icon']}  {item.name}{C.RESET}{run_tag}")

    if depth == 0:
        print()
        pause("Press Enter to go back...")

# ──────────────────────── Search ───────────────────────────────────
def search_files(root: Path):
    clear()
    print_banner()
    
    width = get_terminal_width()
    title = "🔍 Search Files"
    padding = max(0, (width - len(title)) // 2)
    print(" " * padding + f"  {C.WHITE}{C.BOLD}{title}{C.RESET}")
    print_separator()
    query = input(f"  {C.WHITE}Enter filename or extension: {C.RESET}").strip().lower()
    if not query:
        return

    print(f"\n  {C.GRAY}Searching for '{query}'...{C.RESET}\n")
    results = []

    for path in root.rglob("*"):
        if path.is_file():
            skip = False
            for part in path.parts:
                if part in IGNORED_DIRS:
                    skip = True
                    break
            if skip:
                continue
            if path.suffix.lower() in IGNORED_EXT or path.name in IGNORED_FILES:
                continue
            if query in path.name.lower() or query == path.suffix.lower():
                results.append(path)

    if not results:
        print(f"  {C.WHITE}No files found matching '{query}'.{C.RESET}")
        pause()
        return

    print(f"  {C.WHITE}{C.BOLD}Found {len(results)} file(s):{C.RESET}\n")
    for i, p in enumerate(results, 1):
        meta    = file_info(p)
        rel     = p.relative_to(root)
        run_tag = f"  {C.WHITE}[▶]{C.RESET}" if is_runnable(p) else ""
        print(f"  {C.WHITE}[{i:>2}] {meta['icon']}  {rel}{C.RESET}{run_tag}")

    print_separator()
    choice = input(f"\n  {C.WHITE}Enter number to open/run, or press Enter: {C.RESET}").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(results):
            file_action(results[idx])

# ──────────────────────── System Monitor Dashboard ─────────────────
def show_monitor_dashboard():
    """Show system monitoring dashboard."""
    if not MONITOR_AVAILABLE:
        clear()
        print_banner()
        print(f"\n  {C.WHITE}⚠️  System monitoring not available.{C.RESET}")
        print(f"  {C.GRAY}Install psutil: pip install psutil{C.RESET}\n")
        pause()
        return
    
    clear()
    print_banner()
    
    width = get_terminal_width()
    
    # Display dashboard
    sysmon.display_dashboard(width)
    
    print(f"\n  {C.GRAY}Press [R] to refresh, [Enter] to go back{C.RESET}")
    choice = input(f"  {C.WHITE}→ {C.RESET}").strip().lower()
    
    if choice == "r":
        show_monitor_dashboard()  # Recursive refresh

# ──────────────────────── File Action ──────────────────────────────
def file_action(path: Path):
    clear()
    meta = file_info(path)
    
    width = get_terminal_width()  # Get FRESH width for centering
    title = f"{meta['icon']}  {path.name}"
    padding = max(0, (width - len(title)) // 2)
    
    print()
    print(" " * padding + f"{C.WHITE}{C.BOLD}{title}{C.RESET}")
    
    # Center the path too
    path_str = str(path.parent)
    path_padding = max(0, (width - len(path_str)) // 2)
    print(" " * path_padding + f"{C.GRAY}{path_str}{C.RESET}")
    print_separator()

    options = []
    if is_runnable(path):
        options.append(("▶  Run", "run"))
    options.append(("👁  View", "view"))
    options.append(("↩  Back", "back"))

    for i, (label, _) in enumerate(options, 1):
        print(f"  {C.WHITE}[{i}] {label}{C.RESET}")

    print_separator()
    choice = input(f"\n  {C.WHITE}Choose: {C.RESET}").strip()
    if not choice.isdigit():
        return
    idx = int(choice) - 1
    if not (0 <= idx < len(options)):
        return

    action = options[idx][1]

    if action == "back":
        return
    elif action == "view":
        view_file(path)
    elif action == "run":
        run_file(path)

# ──────────────────────── View File ────────────────────────────────
def view_file(path: Path):
    clear()
    meta = file_info(path)
    
    width = get_terminal_width()
    title = f"👁  {path.name}"
    padding = max(0, (width - len(title)) // 2)
    print()
    print(" " * padding + f"  {C.WHITE}{C.BOLD}{title}{C.RESET}")
    print_separator()
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
        lines   = content.splitlines()
        total   = len(lines)
        limit   = 50

        for i, line in enumerate(lines[:limit], 1):
            print(f"  {C.GRAY}{i:>4} │{C.RESET}  {C.WHITE}{line}{C.RESET}")

        if total > limit:
            print(f"\n  {C.GRAY}... ({total - limit} more lines not shown){C.RESET}")
    except Exception as e:
        print(f"  {C.WHITE}Could not read file: {e}{C.RESET}")
    pause()

# ──────────────────────── Run File ─────────────────────────────────
def run_file(path: Path):
    ext = path.suffix.lower()
    clear()
    meta = file_info(path)
    
    width = get_terminal_width()
    title = f"▶  Running: {path.name}"
    padding = max(0, (width - len(title)) // 2)
    print()
    print(" " * padding + f"  {C.WHITE}{C.BOLD}{title}{C.RESET}")
    
    location_text = f"Location: {path.parent}"
    loc_padding = max(0, (width - len(location_text)) // 2)
    print(" " * loc_padding + f"  {C.GRAY}{location_text}{C.RESET}")
    print_separator()
    
    # Show system status if monitoring available
    if MONITOR_AVAILABLE:
        status = sysmon.create_status_bar(width)
        print(f"  {status}")
        print()

    # ── Python ──
    if ext == ".py":
        if not tool_exists("python") and not tool_exists("python3"):
            print(f"  {C.WHITE}Python not found. Install from python.org{C.RESET}")
            pause(); return
        py = "python" if tool_exists("python") else "python3"
        print(f"  {C.GRAY}Running with: {py}{C.RESET}\n")
        
        # Show data flow
        if MONITOR_AVAILABLE:
            sysmon.visualize_data_flow("Python Execution", [
                "📥 Load Python script",
                "🔧 Initialize Python interpreter",
                "⚙️  Execute code line by line",
                "📤 Output results to terminal"
            ])
        
        print_separator()
        
        # Run with monitoring if available
        if MONITOR_AVAILABLE:
            process = subprocess.Popen([py, str(path)], cwd=str(path.parent))
            tracker = sysmon.ProcessTracker(process)
            tracker.start_monitoring()
            process.wait()
            tracker.stop_monitoring()
            stats = tracker.get_stats()
            sysmon.display_execution_report(stats, width)
        else:
            subprocess.run([py, str(path)], cwd=str(path.parent))
        
        print_separator()

    # ── C ──
    elif ext == ".c":
        if not tool_exists("gcc"):
            print(f"  {C.WHITE}gcc not found. Add MinGW to PATH.{C.RESET}")
            pause(); return
        out = path.with_suffix(".exe")
        print(f"  {C.GRAY}Compiling with gcc...{C.RESET}")
        result = subprocess.run(["gcc", str(path), "-o", str(out)], cwd=str(path.parent), capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  {C.WHITE}Compilation error:{C.RESET}\n{result.stderr}")
            pause(); return
        print(f"  {C.WHITE}✔ Compiled successfully!{C.RESET}\n")
        print_separator()
        subprocess.run([str(out)], cwd=str(path.parent))
        print_separator()

    # ── C++ ──
    elif ext == ".cpp":
        if not tool_exists("g++"):
            print(f"  {C.WHITE}g++ not found. Add MinGW to PATH.{C.RESET}")
            pause(); return
        out = path.with_suffix(".exe")
        print(f"  {C.GRAY}Compiling with g++...{C.RESET}")
        result = subprocess.run(["g++", str(path), "-o", str(out)], cwd=str(path.parent), capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  {C.WHITE}Compilation error:{C.RESET}\n{result.stderr}")
            pause(); return
        print(f"  {C.WHITE}✔ Compiled successfully!{C.RESET}\n")
        print_separator()
        subprocess.run([str(out)], cwd=str(path.parent))
        print_separator()

    # ── Java ──
    elif ext == ".java":
        if not tool_exists("javac"):
            print(f"  {C.WHITE}javac not found. Install JDK.{C.RESET}")
            pause(); return
        print(f"  {C.GRAY}Compiling with javac...{C.RESET}")
        
        # Show data flow
        if MONITOR_AVAILABLE:
            sysmon.visualize_data_flow("Java Compilation & Execution", [
                "📥 Load .java source file",
                "🔧 Compile with javac → .class bytecode",
                "⚙️  JVM loads bytecode",
                "🚀 Execute in Java Virtual Machine",
                "📤 Output results"
            ])
        
        result = subprocess.run(["javac", str(path)], cwd=str(path.parent), capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  {C.WHITE}Compilation error:{C.RESET}\n{result.stderr}")
            pause(); return
        print(f"  {C.WHITE}✔ Compiled successfully!{C.RESET}\n")
        class_name = path.stem
        print_separator()
        
        # Run with monitoring
        if MONITOR_AVAILABLE:
            process = subprocess.Popen(["java", class_name], cwd=str(path.parent))
            tracker = sysmon.ProcessTracker(process)
            tracker.start_monitoring()
            process.wait()
            tracker.stop_monitoring()
            stats = tracker.get_stats()
            sysmon.display_execution_report(stats, width)
        else:
            subprocess.run(["java", class_name], cwd=str(path.parent))
        
        print_separator()

    # ── JavaScript ──
    elif ext == ".js":
        if not tool_exists("node"):
            print(f"  {C.WHITE}Node.js not found. Install from nodejs.org{C.RESET}")
            pause(); return
        print(f"  {C.GRAY}Running with node...{C.RESET}\n")
        
        # Show data flow
        if MONITOR_AVAILABLE:
            sysmon.visualize_data_flow("Node.js Execution", [
                "📥 Load JavaScript file",
                "🔧 Initialize V8 JavaScript engine",
                "⚙️  Parse and execute code",
                "📤 Output to console"
            ])
        
        print_separator()
        
        # Run with monitoring
        if MONITOR_AVAILABLE:
            process = subprocess.Popen(["node", str(path)], cwd=str(path.parent))
            tracker = sysmon.ProcessTracker(process)
            tracker.start_monitoring()
            process.wait()
            tracker.stop_monitoring()
            stats = tracker.get_stats()
            sysmon.display_execution_report(stats, width)
        else:
            subprocess.run(["node", str(path)], cwd=str(path.parent))
        
        print_separator()

    # ── TypeScript ──
    elif ext == ".ts":
        if not tool_exists("ts-node") and not tool_exists("npx"):
            print(f"  {C.WHITE}ts-node not found. Run: npm install -g ts-node{C.RESET}")
            pause(); return
        runner = ["ts-node", str(path)] if tool_exists("ts-node") else ["npx", "ts-node", str(path)]
        print(f"  {C.GRAY}Running TypeScript...{C.RESET}\n")
        print_separator()
        subprocess.run(runner, cwd=str(path.parent))
        print_separator()

    # ── HTML ──
    elif ext == ".html":
        print(f"  {C.GRAY}Opening in default browser...{C.RESET}")
        webbrowser.open(path.as_uri())
        print(f"  {C.WHITE}✔ Opened {path.name} in browser!{C.RESET}")

    # ── SQL ──
    elif ext == ".sql":
        print(f"  {C.WHITE}💡 SQL files need a database connection to run.{C.RESET}")
        print(f"  {C.GRAY}Showing file contents instead:{C.RESET}\n")
        print_separator()
        view_file(path)
        return

    # ── Arduino ──
    elif ext == ".ino":
        print(f"  {C.WHITE}💡 Arduino sketches need Arduino IDE to run.{C.RESET}")
        print(f"  {C.GRAY}Showing sketch contents instead:{C.RESET}\n")
        print_separator()
        view_file(path)
        return

    # ── Jupyter ──
    elif ext == ".ipynb":
        if tool_exists("jupyter"):
            print(f"  {C.GRAY}Opening in Jupyter Notebook...{C.RESET}")
            subprocess.Popen(["jupyter", "notebook", str(path)], cwd=str(path.parent))
            print(f"  {C.WHITE}✔ Jupyter launched!{C.RESET}")
        else:
            print(f"  {C.WHITE}Jupyter not found. Showing raw content...{C.RESET}\n")
            view_file(path)
            return

    # ── PHP ──
    elif ext == ".php":
        if not tool_exists("php"):
            print(f"  {C.WHITE}PHP not found. Install PHP.{C.RESET}")
            pause(); return
        print(f"  {C.GRAY}Running with php...{C.RESET}\n")
        print_separator()
        subprocess.run(["php", str(path)], cwd=str(path.parent))
        print_separator()

    # ── Kotlin ──
    elif ext == ".kt":
        if not tool_exists("kotlinc"):
            print(f"  {C.WHITE}kotlinc not found. Install Kotlin.{C.RESET}")
            pause(); return
        jar_out = path.with_suffix(".jar")
        print(f"  {C.GRAY}Compiling Kotlin...{C.RESET}")
        result = subprocess.run(["kotlinc", str(path), "-include-runtime", "-d", str(jar_out)],
                                cwd=str(path.parent), capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  {C.WHITE}Compilation error:{C.RESET}\n{result.stderr}")
            pause(); return
        print(f"  {C.WHITE}✔ Compiled!{C.RESET}\n")
        print_separator()
        subprocess.run(["java", "-jar", str(jar_out)], cwd=str(path.parent))
        print_separator()

    else:
        print(f"  {C.WHITE}No runner configured for '{ext}' files.{C.RESET}")

    pause()

# ──────────────────────── Main Loop ────────────────────────────────
def main():
    current = ROOT
    history = []

    while True:
        result = list_directory_view(current, history)

        if result is None:
            continue
        elif result == "quit":
            clear()
            width = get_terminal_width()
            goodbye = "👋 Goodbye from Code Vault CLI!"
            padding = max(0, (width - len(goodbye)) // 2)
            print()
            print(" " * padding + f"  {C.WHITE}{C.BOLD}{goodbye}{C.RESET}")
            print()
            sys.exit(0)
        elif result == "back":
            if history:
                current = history.pop()
        elif result == "home":
            history.clear()
            current = ROOT
        elif result == "tree":
            clear()
            print_banner()
            depth_input = input(f"  {C.WHITE}Max depth to show (1-5, default=3): {C.RESET}").strip()
            depth = int(depth_input) if depth_input.isdigit() and 1 <= int(depth_input) <= 5 else 3
            clear()
            tree_view(current, max_depth=depth)
        elif result == "search":
            search_files(ROOT)
        elif result == "monitor":
            show_monitor_dashboard()
        elif isinstance(result, tuple):
            action, path = result
            if action == "enter":
                history.append(current)
                current = path
            elif action == "file":
                file_action(path)

if __name__ == "__main__":
    main()
