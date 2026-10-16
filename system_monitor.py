"""
╔══════════════════════════════════════════════════════════╗
║         System Monitor Module for DHRUVIN's CLI          ║
║       RAM, CPU, Storage, Network, Process Tracking       ║
╚══════════════════════════════════════════════════════════╝
"""

import psutil
import time
import threading
from datetime import datetime

# ANSI Colors
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    WHITE   = "\033[97m"
    GRAY    = "\033[37m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    CYAN    = "\033[96m"
    BLUE    = "\033[94m"

# ──────────────────────── Progress Bar ────────────────────────────
def draw_bar(percentage, width=20, fill_char="█", empty_char="░"):
    """Draw a progress bar with percentage."""
    filled = int(width * percentage / 100)
    empty = width - filled
    
    # Color based on percentage
    if percentage < 50:
        color = C.GREEN
    elif percentage < 80:
        color = C.YELLOW
    else:
        color = C.RED
    
    bar = f"{color}{fill_char * filled}{C.GRAY}{empty_char * empty}{C.RESET}"
    return f"[{bar}] {percentage:5.1f}%"

# ──────────────────────── System Stats ─────────────────────────────
def get_ram_usage():
    """Get RAM usage statistics."""
    mem = psutil.virtual_memory()
    return {
        "percent": mem.percent,
        "used_gb": mem.used / (1024**3),
        "total_gb": mem.total / (1024**3),
        "available_gb": mem.available / (1024**3)
    }

def get_cpu_usage():
    """Get CPU usage statistics."""
    cpu_percent = psutil.cpu_percent(interval=0.1)
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    
    return {
        "percent": cpu_percent,
        "count": cpu_count,
        "freq_mhz": cpu_freq.current if cpu_freq else 0
    }

def get_storage_usage(path="d:/"):
    """Get storage usage for a specific drive."""
    try:
        disk = psutil.disk_usage(path)
        return {
            "percent": disk.percent,
            "used_gb": disk.used / (1024**3),
            "total_gb": disk.total / (1024**3),
            "free_gb": disk.free / (1024**3)
        }
    except:
        return {"percent": 0, "used_gb": 0, "total_gb": 0, "free_gb": 0}

def get_network_io():
    """Get network I/O statistics."""
    net = psutil.net_io_counters()
    return {
        "sent_mb": net.bytes_sent / (1024**2),
        "recv_mb": net.bytes_recv / (1024**2),
        "packets_sent": net.packets_sent,
        "packets_recv": net.packets_recv
    }

# ──────────────────────── Status Bar ───────────────────────────────
def create_status_bar(width=120):
    """Create a compact status bar with system info."""
    ram = get_ram_usage()
    cpu = get_cpu_usage()
    storage = get_storage_usage()
    
    # Compact display
    ram_str = f"RAM: {ram['percent']:4.1f}%"
    cpu_str = f"CPU: {cpu['percent']:4.1f}%"
    storage_str = f"Storage: {storage['percent']:4.1f}%"
    time_str = datetime.now().strftime("%H:%M:%S")
    
    # Color coding
    ram_color = C.GREEN if ram['percent'] < 70 else (C.YELLOW if ram['percent'] < 85 else C.RED)
    cpu_color = C.GREEN if cpu['percent'] < 70 else (C.YELLOW if cpu['percent'] < 85 else C.RED)
    storage_color = C.GREEN if storage['percent'] < 70 else (C.YELLOW if storage['percent'] < 85 else C.RED)
    
    status = (f"{C.GRAY}[{C.WHITE}{time_str}{C.GRAY}]  "
              f"{ram_color}{ram_str}{C.RESET}  "
              f"{cpu_color}{cpu_str}{C.RESET}  "
              f"{storage_color}{storage_str}{C.RESET}")
    
    return status

# ──────────────────────── Dashboard View ───────────────────────────
def display_dashboard(width=120):
    """Display full system monitoring dashboard."""
    ram = get_ram_usage()
    cpu = get_cpu_usage()
    storage = get_storage_usage()
    net = get_network_io()
    
    # Title
    title = "⚡ SYSTEM MONITOR DASHBOARD"
    padding = max(0, (width - len(title)) // 2)
    print()
    print(" " * padding + f"{C.WHITE}{C.BOLD}{title}{C.RESET}")
    print(f"{C.WHITE}{'═' * width}{C.RESET}")
    print()
    
    # RAM Module
    print(f"  {C.CYAN}{C.BOLD}💾 MEMORY (RAM){C.RESET}")
    print(f"    {draw_bar(ram['percent'], width=40)}")
    print(f"    {C.WHITE}Used: {ram['used_gb']:.2f} GB  /  Total: {ram['total_gb']:.2f} GB  /  Available: {ram['available_gb']:.2f} GB{C.RESET}")
    print()
    
    # CPU Module
    print(f"  {C.CYAN}{C.BOLD}🔥 PROCESSOR (CPU){C.RESET}")
    print(f"    {draw_bar(cpu['percent'], width=40)}")
    print(f"    {C.WHITE}Cores: {cpu['count']}  |  Frequency: {cpu['freq_mhz']:.0f} MHz  |  Usage: {cpu['percent']:.1f}%{C.RESET}")
    print()
    
    # Storage Module
    print(f"  {C.CYAN}{C.BOLD}💿 STORAGE (D: Drive){C.RESET}")
    print(f"    {draw_bar(storage['percent'], width=40)}")
    print(f"    {C.WHITE}Used: {storage['used_gb']:.1f} GB  /  Total: {storage['total_gb']:.1f} GB  /  Free: {storage['free_gb']:.1f} GB{C.RESET}")
    print()
    
    # Network Module
    print(f"  {C.CYAN}{C.BOLD}🌐 NETWORK I/O{C.RESET}")
    print(f"    {C.WHITE}↑ Sent: {net['sent_mb']:.1f} MB  ({net['packets_sent']:,} packets){C.RESET}")
    print(f"    {C.WHITE}↓ Received: {net['recv_mb']:.1f} MB  ({net['packets_recv']:,} packets){C.RESET}")
    print()
    
    print(f"{C.WHITE}{'═' * width}{C.RESET}")

# ──────────────────────── Process Tracker ──────────────────────────
class ProcessTracker:
    """Track resource usage of a running process."""
    
    def __init__(self, process):
        self.process = process
        self.start_time = time.time()
        self.cpu_samples = []
        self.mem_samples = []
        self.running = True
        self.monitor_thread = None
    
    def start_monitoring(self):
        """Start monitoring in background thread."""
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
    
    def _monitor_loop(self):
        """Background monitoring loop."""
        try:
            proc = psutil.Process(self.process.pid)
            while self.running and self.process.poll() is None:
                try:
                    cpu = proc.cpu_percent(interval=0.5)
                    mem = proc.memory_info().rss / (1024**2)  # MB
                    self.cpu_samples.append(cpu)
                    self.mem_samples.append(mem)
                except:
                    break
                time.sleep(0.5)
        except:
            pass
    
    def stop_monitoring(self):
        """Stop monitoring."""
        self.running = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=1)
    
    def get_stats(self):
        """Get monitoring statistics."""
        elapsed = time.time() - self.start_time
        
        avg_cpu = sum(self.cpu_samples) / len(self.cpu_samples) if self.cpu_samples else 0
        max_cpu = max(self.cpu_samples) if self.cpu_samples else 0
        
        avg_mem = sum(self.mem_samples) / len(self.mem_samples) if self.mem_samples else 0
        max_mem = max(self.mem_samples) if self.mem_samples else 0
        
        return {
            "elapsed_sec": elapsed,
            "avg_cpu": avg_cpu,
            "max_cpu": max_cpu,
            "avg_mem_mb": avg_mem,
            "max_mem_mb": max_mem,
            "samples": len(self.cpu_samples)
        }

# ──────────────────────── Data Flow Visualizer ─────────────────────
def visualize_data_flow(operation, steps):
    """
    Visualize data flow for an operation.
    
    Args:
        operation: Name of the operation
        steps: List of step descriptions
    """
    print()
    print(f"  {C.CYAN}{C.BOLD}📊 DATA FLOW: {operation}{C.RESET}")
    print(f"  {C.GRAY}{'─' * 60}{C.RESET}")
    
    for i, step in enumerate(steps, 1):
        if i < len(steps):
            connector = "  │"
            print(f"  {C.WHITE}[{i}] {step}{C.RESET}")
            print(f"  {C.GRAY}{connector}{C.RESET}")
            print(f"  {C.GRAY}{'  ↓'}{C.RESET}")
            print(f"  {C.GRAY}{connector}{C.RESET}")
        else:
            print(f"  {C.WHITE}[{i}] {step}{C.RESET}")
    
    print(f"  {C.GRAY}{'─' * 60}{C.RESET}")
    print(f"  {C.GREEN}✓ Flow Complete{C.RESET}")
    print()

# ──────────────────────── Execution Report ─────────────────────────
def display_execution_report(stats, width=120):
    """Display execution statistics report."""
    print()
    print(f"{C.WHITE}{'═' * width}{C.RESET}")
    print(f"  {C.CYAN}{C.BOLD}📈 EXECUTION REPORT{C.RESET}")
    print(f"{C.WHITE}{'═' * width}{C.RESET}")
    
    elapsed_min = stats['elapsed_sec'] / 60
    elapsed_str = f"{elapsed_min:.2f} min" if elapsed_min >= 1 else f"{stats['elapsed_sec']:.2f} sec"
    
    print(f"  {C.WHITE}⏱️  Execution Time: {elapsed_str}{C.RESET}")
    print(f"  {C.WHITE}📊 Samples Collected: {stats['samples']}{C.RESET}")
    print()
    
    print(f"  {C.CYAN}{C.BOLD}CPU Usage:{C.RESET}")
    print(f"    Average: {draw_bar(stats['avg_cpu'], width=30)}")
    print(f"    Peak:    {draw_bar(stats['max_cpu'], width=30)}")
    print()
    
    print(f"  {C.CYAN}{C.BOLD}Memory Usage:{C.RESET}")
    print(f"    {C.WHITE}Average: {stats['avg_mem_mb']:.1f} MB{C.RESET}")
    print(f"    {C.WHITE}Peak:    {stats['max_mem_mb']:.1f} MB{C.RESET}")
    print()
    
    print(f"{C.WHITE}{'═' * width}{C.RESET}")

# ──────────────────────── Helper Functions ─────────────────────────
def get_system_summary():
    """Get a one-line system summary."""
    ram = get_ram_usage()
    cpu = get_cpu_usage()
    
    return f"RAM: {ram['percent']:.0f}% | CPU: {cpu['percent']:.0f}%"

def is_system_healthy():
    """Check if system resources are healthy."""
    ram = get_ram_usage()
    cpu = get_cpu_usage()
    
    return ram['percent'] < 90 and cpu['percent'] < 90
