# ⚡ System Monitor & Resource Tracker Guide

## 🎯 What's New in Your CLI

Your CLI now includes **real-time system monitoring** and **execution tracking**! See exactly what resources your code uses while it runs.

---

## ✨ New Features

### 1. **System Monitor Dashboard** 📊
Press `[M]` from anywhere to view:
- 💾 **RAM Usage** - Live memory consumption with color-coded bar
- 🔥 **CPU Usage** - Processor utilization with multi-core info  
- 💿 **Storage** - D: drive space with used/free breakdown
- 🌐 **Network I/O** - Data sent/received since boot

### 2. **Execution Tracking** 🏃
When running code files (Python, Java, JavaScript):
- Real-time CPU monitoring during execution
- Memory usage tracking
- Average and peak resource metrics
- Execution time measurement

### 3. **Data Flow Visualization** 📊
Visual step-by-step breakdown showing:
- Where data comes from
- How it's processed
- Where results go
- Clear flowchart-style display

### 4. **Live Status Bar** ⚡
System status shown before running code:
- Current RAM percentage
- Current CPU percentage
- Current storage usage
- Live timestamp

---

## 🎮 How to Use

### **View System Dashboard:**
```
1. Run: run_cli.bat
2. Press: M
3. See: Full system metrics
4. Press: R (to refresh) or Enter (to go back)
```

### **Monitor Code Execution:**
```
1. Navigate to a Python/Java/JS file
2. Select [▶ Run]
3. Watch:
   - Data flow visualization
   - Code execution
   - Performance report (CPU, RAM, time)
```

---

## 📊 Visual Examples

### **System Dashboard:**
```
⚡ SYSTEM MONITOR DASHBOARD
════════════════════════════════════════════════════════

💾 MEMORY (RAM)
  [████████████████████████░░░░] 75.5%
  Used: 6.04 GB / Total: 8.00 GB / Available: 1.96 GB

🔥 PROCESSOR (CPU)
  [██████████░░░░░░░░░░░░░░░░░░] 35.2%
  Cores: 8 | Frequency: 3600 MHz | Usage: 35.2%

💿 STORAGE (D: Drive)
  [████████████████░░░░░░░░░░░░] 62.3%
  Used: 186.9 GB / Total: 300.0 GB / Free: 113.1 GB

🌐 NETWORK I/O
  ↑ Sent: 1234.5 MB (456,789 packets)
  ↓ Received: 5678.9 MB (987,654 packets)
```

### **Data Flow Visualization:**
```
📊 DATA FLOW: Python Execution
────────────────────────────────────────────────────────
[1] 📥 Load Python script
  │
  ↓
  │
[2] 🔧 Initialize Python interpreter
  │
  ↓
  │
[3] ⚙️  Execute code line by line
  │
  ↓
  │
[4] 📤 Output results to terminal
────────────────────────────────────────────────────────
✓ Flow Complete
```

### **Execution Report:**
```
════════════════════════════════════════════════════════
📈 EXECUTION REPORT
════════════════════════════════════════════════════════
⏱️  Execution Time: 3.45 sec
📊 Samples Collected: 7

CPU Usage:
  Average: [██████░░░░░░░░░░░░░░░░░░] 25.3%
  Peak:    [████████████░░░░░░░░░░░░] 45.8%

Memory Usage:
  Average: 52.3 MB
  Peak:    68.7 MB
```

---

## 🎨 Color Coding

| Metric | Color | Meaning |
|--------|-------|---------|
| **0-50%** | 🟢 Green | Healthy, plenty of resources |
| **50-80%** | 🟡 Yellow | Moderate usage, monitor closely |
| **80-100%** | 🔴 Red | High usage, may slow down |

---

## 🚀 Supported Languages

**Full monitoring support:**
- ✅ **Python** (.py)
- ✅ **Java** (.java)
- ✅ **JavaScript** (.js)

**Basic support** (no process tracking):
- ⚠️ C/C++ (compiled executables)
- ⚠️ Others (direct subprocess execution)

---

## 📋 Key Metrics Explained

### **RAM (Memory)**
- **Used**: Currently allocated to programs
- **Available**: Ready for new programs
- **Total**: Physical RAM installed

### **CPU (Processor)**
- **Usage %**: How busy the processor is
- **Cores**: Number of logical processors
- **Frequency**: Current clock speed in MHz

### **Storage (Disk)**
- **Used**: Files taking up space
- **Free**: Available for new files
- **Total**: Drive capacity

### **Network I/O**
- **Sent**: Data uploaded since boot
- **Received**: Data downloaded since boot
- **Packets**: Individual network messages

---

## 🛠️ Technical Details

### **Monitoring Technology:**
- **Library**: `psutil` 7.2.2
- **Update Interval**: 0.5 seconds
- **Overhead**: <1% CPU impact
- **Thread-safe**: Runs in background

### **Process Tracking:**
- Captures CPU% every 0.5s
- Records memory usage (RSS)
- Calculates average and peak
- Non-intrusive monitoring

### **Data Flow:**
- Predefined flow templates per language
- Shows compilation → execution → output
- Visual flowchart representation

---

## ⚙️ Configuration

### **Disable Monitoring:**
If you want to run without monitoring (faster startup):
1. Rename `system_monitor.py` to `system_monitor.py.bak`
2. CLI will work normally without [M] option

### **Re-enable Monitoring:**
1. Rename back to `system_monitor.py`
2. Ensure psutil is installed: `pip install psutil`

---

## 💡 Pro Tips

1. **Before Running Heavy Code**: Check `[M]` dashboard to see available resources
2. **Compare Runs**: Note execution time and peak RAM to optimize code
3. **Refresh Dashboard**: Press `R` repeatedly to watch real-time changes
4. **Health Check**: If metrics are red, close other programs first
5. **Benchmark**: Use execution reports to compare algorithm performance

---

## 🐛 Troubleshooting

### **"Monitor not available" message:**
```bash
# Install psutil in portable Python
cd d:\Codes
.\python_portable\Scripts\pip.exe install psutil
```

### **Monitor shows 0% for everything:**
- Restart the CLI
- Check psutil installation
- Try refreshing the dashboard with `[R]`

### **Execution report not showing:**
- Only works for Python, Java, JavaScript
- Must run from within the CLI (not external terminal)
- Process must complete normally

---

## 📊 What to Watch For

### **High RAM (>85%):**
- 💡 Close unnecessary programs
- 💡 Consider upgrading RAM
- 💡 Optimize code to use less memory

### **High CPU (>90%):**
- 💡 Code is compute-intensive (expected for some operations)
- 💡 May slow down other programs
- 💡 Consider algorithm optimization

### **High Storage (>90%):**
- 💡 Clean up old files
- 💡 Move projects to external drive
- 💡 Empty recycle bin

---

## 🎓 Example Workflow

**Scenario: Running a Python script**

1. **Check resources first:**
   ```
   Press [M] → See RAM: 45%, CPU: 20% → Good to go!
   ```

2. **Navigate to script:**
   ```
   Find your Python file → Press number
   ```

3. **Run with monitoring:**
   ```
   Select [▶ Run] → Watch:
   - Status bar shows current system state
   - Data flow shows execution steps
   - Code runs
   - Execution report shows performance
   ```

4. **Analyze results:**
   ```
   Execution Time: 2.3 sec
   Peak CPU: 55% → Script is efficient
   Peak RAM: 120 MB → Memory usage is reasonable
   ```

---

## 🎉 Benefits

✨ **Performance Insights** - Know exactly how your code behaves  
✨ **Resource Awareness** - Avoid running heavy code on low resources  
✨ **Optimization Guide** - Identify bottlenecks and improve code  
✨ **System Health** - Monitor overall computer performance  
✨ **Learning Tool** - Understand what happens when code runs  

---

## 📚 Related Files

- **`system_monitor.py`** - Core monitoring module
- **`cli.py`** - Main CLI with monitoring integration
- **`test_monitor.py`** - Test script for verification

---

**Ready to monitor your code like a pro! ⚡**

*Last updated: August 13, 2026*
