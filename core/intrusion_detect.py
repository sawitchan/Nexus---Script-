import time
import os

LOG_FILE = "access.log"
# Daftar folder yang biasanya diincar Hacker
SENSITIVE_PATHS = ["/admin", "/wp-admin", "/.env", "/config", "/phpmyadmin", "/setup.php"]

def sniff_intrusion():
    print("\033[1;35m[*] INTRUSION DETECTION SYSTEM (IDS) ACTIVE...\033[0m")
    if not os.path.exists(LOG_FILE): return

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    
    # Kosongkan log setelah dibaca (opsional, agar tidak dobel)
    # with open(LOG_FILE, "w") as f: f.write("")

    for line in lines:
        for path in SENSITIVE_PATHS:
            if path in line:
                parts = line.split()
                ip = parts[0] if parts else "Unknown"
                print(f"\033[1;31m[!!!] INTRUSION ATTEMPT: {ip} tried to access {path}\033[0m")
                # Otomatis lempar ke blacklist
                with open("blocked_ips.txt", "a") as b:
                    b.write(f"{ip}\n")

if __name__ == "__main__":
    while True:
        sniff_intrusion()
        time.sleep(5)
