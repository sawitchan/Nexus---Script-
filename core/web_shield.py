import time
import os

# --- KONFIGURASI REAL ---
LOG_FILE = "access.log" 
THRESHOLD = 20  
ips_count = {}

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f: f.write("")

def block_ip(ip):
    print(f"\033[1;31m[!] EXECUTING FIREWALL BLOCK: {ip}\033[0m")
    with open("blocked_ips.txt", "a") as f:
        f.write(f"{ip}\n")

def scan_log():
    print(f"\033[1;32m[*] REAL-TIME MONITORING: {LOG_FILE}...\033[0m")
    while True:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                lines = f.readlines()
            
            # Reset log setelah dibaca agar tidak dibaca berulang (Real Logic)
            with open(LOG_FILE, "w") as f: f.write("")

            for line in lines:
                parts = line.split()
                if parts:
                    ip = parts[0]
                    ips_count[ip] = ips_count.get(ip, 0) + 1
                    if ips_count[ip] > THRESHOLD:
                        block_ip(ip)
                        ips_count[ip] = 0
        time.sleep(1)

if __name__ == "__main__":
    try:
        scan_log()
    except KeyboardInterrupt:
        print("\n[!] Shield Deactivated.")
