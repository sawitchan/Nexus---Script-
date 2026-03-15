from core.ghost_engine import get_global_proxy
import requests

print("\033[1;32m[*] Memulai Ghost Health Check...\033[0m")
proxy = get_global_proxy()

if proxy:
    print(f"\033[1;34m[GHOST] Jalur Aktif: {proxy['info']}\033[0m")
    try:
        # Melakukan pengecekan koneksi sistem via Proxy
        res = requests.get("https://google.com", proxies=proxy, timeout=5)
        print(f"[+] System Status: ONLINE (Via Proxy)")
    except:
        print("[!] Proxy Slow/Down. Mencari jalur lain...")
else:
    print("\033[1;31m[!] Gagal mendapatkan jalur Ghost Proxy.\033[0m")
