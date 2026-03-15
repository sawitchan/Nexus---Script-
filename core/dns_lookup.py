import sys
import os
import requests
import random

def auto_dns():
    print("\033[1;36m" + "="*45)
    print("     NEXUS-OMNI DNS")
    print("="*45 + "\033[0m")
    
    domain = input("[?] Masukkan Domain Target: ").strip()
    proxy_file = "proxyscrape_premium_http_proxies.txt"
    
    if os.path.exists(proxy_file):
        with open(proxy_file, "r") as f:
            proxies_list = [l.strip() for l in f if l.strip() and not l.startswith('[')]
        selected = random.choice(proxies_list)
        proxies = {"http": f"http://{selected}", "https": f"http://{selected}"}
        print(f"\033[1;33m[*] Menggunakan Jalur Anonim: {selected}\033[0m")
    else: return

    try:
        url = f"https://cloudflare-dns.com/query?name={domain}&type=A"
        # Request otomatis lewat jalur Ghost
        res = requests.get(url, proxies=proxies, timeout=10).json()
        print(f"\n\033[1;32m[+] Intelijen DNS Berhasil Ditarik:\033[0m")
        for record in res.get("Answer", []):
            print(f" -> Result: {record['data']}")
    except:
        print("\033[1;31m[!] Jalur terdeteksi! Mengalihkan ke Proxy lain...\033[0m")

if __name__ == "__main__":
    auto_dns()
