import time
import os

BLACKLIST_FILE = "blocked_ips.txt"
HTACCESS_FILE = ".htaccess" # Simulasi file proteksi web

def update_firewall():
    if os.path.exists(BLACKLIST_FILE):
        with open(BLACKLIST_FILE, "r") as f:
            ips = f.read().splitlines()
        
        # Ambil IP unik saja
        unique_ips = list(set(ips))
        
        print(f"\033[1;33m[*] SYNCING FIREWALL: {len(unique_ips)} IPs detected...\033[0m")
        
        # Tulis ke format .htaccess (Standar Web Security)
        with open(HTACCESS_FILE, "w") as f:
            f.write("# NEXUS-OMNI AUTO BLOCK\n")
            for ip in unique_ips:
                f.write(f"Deny from {ip}\n")
        
        print("\033[1;32m[+] FIREWALL UPDATED SUCCESSFULLY!\033[0m")

if __name__ == "__main__":
    while True:
        update_firewall()
        time.sleep(10) # Update tiap 10 detik
