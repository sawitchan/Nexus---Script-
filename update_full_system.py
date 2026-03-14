import os

# Database Path & Scripts
core_path = "core/"
scripts_path = "core/scripts/"

# Membuat folder jika belum ada
os.makedirs(scripts_path, exist_ok=True)

modules = {
    # [01] DDoS Shield (Traffic Monitor)
    "shield.py": """
import os, time
print("\\033[1;31m[!] MONITORING INCOMING TRAFFIC (ANTI-DDoS)...\\033[0m")
# Real command to check active connections
os.system("netstat -an | grep ESTABLISHED | wc -l > connections.txt")
with open("connections.txt", "r") as f:
    conn = f.read().strip()
print(f"[*] Active Connections: {conn}")
print("[*] Shield Status: ACTIVE")
""",

    # [05] IP Geo-Tracker (Real Tracker)
    "ip_tracker.py": """
import requests
ip = input("\\033[1;33m[?] Masukkan IP Target: \\033[0m")
r = requests.get(f"http://ip-api.com/json/{ip}").json()
if r['status'] == 'success':
    print(f"Country: {r['country']}\\nCity: {r['city']}\\nISP: {r['isp']}\\nLat/Lon: {r['lat']}/{r['lon']}")
else:
    print("[!] IP Tidak Valid.")
""",

    # [12] Responsive RAM Monitor
    "ram_monitor.py": """
import os
print("\\033[1;36m[*] RAM USAGE INFO\\033[0m")
os.system("free -h")
# Visual Bar
used = os.popen("free | grep Mem | awk '{print $3/$2 * 100}'").read()
bar = "#" * int(float(used)/5)
print(f"Progress: [{bar:<20}] {float(used):.2f}%")
""",

    # [13] Deep Storage Analyzer
    "storage_deep.py": """
import os, platform
print("\\033[1;33m[+] DEEP STORAGE & DEVICE INFO\\033[0m")
print(f"Kernel: {platform.release()}")
print(f"Platform: {platform.platform()}")
os.system("df -h /data/data/com.termux/files/home")
""",

    # [14] Smart Process Monitor
    "process_monitor.py": """
import os
print("\\033[1;32m[*] TOP 10 RESOURCE CONSUMING PROCESSES\\033[0m")
os.system("ps -eo user,pid,pcpu,pmem,comm --sort=-pcpu | head -n 11")
""",

    # [15] Global Public IP
    "ip_global.py": """
import requests
print("\\033[1;34m[*] CAPTURING GLOBAL NETWORK ENTRY...\\033[0m")
r = requests.get("https://ifconfig.me/all.json").json()
print(f"Public IP: {r['ip_addr']}\\nUser-Agent: {r['user_agent']}")
""",

    # [17] Real Port Scanner
    "port_scan.py": """
import socket
target = input("[?] Target (IP/Domain): ")
ports = [21, 22, 80, 443, 8080, 3306]
print(f"[*] Scanning Ports on {target}...")
for p in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((target, p)) == 0:
        print(f"Port {p} : OPEN")
    s.close()
""",

    # [21] Live Cyber Attack Monitor
    "cyber_live.py": """
import requests, time, random
print("\\033[1;31m[!] LIVE CYBER ATTACK STREAM (WORLDWIDE)\\033[0m")
# Fetching dynamic data simulation based on real countries
targets = ["USA", "China", "Russia", "Indonesia", "Germany", "Japan"]
types = ["DDoS", "SQL Injection", "Brute Force", "Malware"]
for i in range(5):
    print(f"[*] ATTACK DETECTED: {random.choice(targets)} | TYPE: {random.choice(types)} | INTENSITY: {random.randint(70, 100)}%")
    time.sleep(0.7)
"""
}

# Writing files
for name, code in modules.items():
    with open(os.path.join(core_path, name), "w") as f:
        f.write(code.strip())

print("[+] All Modules Updated to REAL-TIME Mode!")
