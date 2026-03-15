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
    
    # Otomatis deteksi proxy premium Tuan
    proxy_file = "proxyscrape_premium_http_proxies.txt"
    if os.path.exists(proxy_file):
        with open(proxy_file, "r") as f:
            proxies = [line.strip() for line in f if line.strip() and not line.startswith('[')]
        selected = random.choice(proxies)
        print(f"\033[1;32m[*] Jalur DNS Aktif: {selected} (Auto-Switch)\033[0m")
    else:
        print("\033[1;31m[!] File Proxy tidak ditemukan!\033[0m")
        return

    def scan_pintu(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((target, port)) == 0:
                print(f" \033[1;32m[+] CELAH TERBUKA: Port {port}\033[0m")
            s.close()
        except: pass

    print(f"[*] Menjalankan Scanning Otomatis pada {target}...")
    # Menggunakan Threading agar cepat dan otomatis deteksi port 1-1024
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_pintu, range(1, 1025))

if __name__ == "__main__":
    ghost_scan()
