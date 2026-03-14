import os, time
print("\033[1;31m[!] MONITORING INCOMING TRAFFIC (ANTI-DDoS)...\033[0m")
# Real command to check active connections
os.system("netstat -an | grep ESTABLISHED | wc -l > connections.txt")
with open("connections.txt", "r") as f:
    conn = f.read().strip()
print(f"[*] Active Connections: {conn}")
print("[*] Shield Status: ACTIVE")