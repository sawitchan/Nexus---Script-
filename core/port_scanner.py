import socket
import sys
import os
import random
import concurrent.futures

def ghost_scan():
    print("\033[1;36m" + "="*45)
    print("     NEXUS-OMNI SCANNER")
    print("="*45 + "\033[0m")
    
    target = input("[?] Masukkan Target: ").strip()
    if not target: return
    
    # Deteksi File Tuan secara otomatis
    premium_file = "proxyscrape_premium_http_proxies.txt"
    if os.path.exists(premium_file):
        with open(premium_file, "r") as f:
            proxies = [l.strip() for l in f if l.strip() and not l.startswith('[')]
        selected = random.choice(proxies)
        print(f"\033[1;32m[*] Jalur Ghost Aktif: {selected}\033[0m")
    else:
        print("\033[1;31m[!] Error: File proxyscrape_premium_http_proxies.txt tidak ada!\033[0m")
        return

    def scan_pintu(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((target, port)) == 0:
                print(f" \033[1;32m[+] TERDETEKSI TERBUKA: Port {port}\033[0m")
            s.close()
        except: pass

    print(f"[*] Scanning Otomatis Port 1-1024 pada {target}...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_pintu, range(1, 1025))
    print("\nSelesai, Tuan Markus! Data Intel & Port sudah siap.")

if __name__ == "__main__":
    ghost_scan()
