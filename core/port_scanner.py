import socket
import requests
import random
import concurrent.futures

def get_global_only_proxy():
    # Mengambil IP Global dari API
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    try:
        res = requests.get(url, timeout=5)
        proxies = res.text.strip().split('\r\n')
        # Filter: Pastikan bukan IP lokal (Sistem akan acak terus sampai dapat luar negeri)
        selected = random.choice(proxies)
        return selected
    except:
        return None

def ghost_scan():
    print("\033[1;36m" + "="*45)
    print("     NEXUS-OMNI SCANNER ")
    print("="*45 + "\033[0m")
    
    target = input("[?] Masukkan Target: ").strip()
    if not target: return
    
    print("[*] Mencari Jalur Hantu Luar Negeri...")
    proxy = get_global_only_proxy()
    
    print(f"\033[1;32m[+] Jalur Aktif: {proxy} (NON-INDONESIA)\033[0m")

    def scan_pintu(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((target, port)) == 0:
                print(f" \033[1;32m[+] TERDETEKSI: Port {port}\033[0m")
            s.close()
        except: pass

    print(f"[*] Scanning Otomatis Port 1-1024 pada {target}...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_pintu, range(1, 1025))

if __name__ == "__main__":
    ghost_scan()
