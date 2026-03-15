import sys
import os
import requests
import random

def auto_dns():
    print("\033[1;36m" + "="*45)
    print("     NEXUS-OMNI DNS")
    print("="*45 + "\033[0m")
    
    domain = input("[?] Masukkan Domain Target: ").strip()
    if not domain: return

    premium_file = "proxyscrape_premium_http_proxies.txt"
    if os.path.exists(premium_file):
        with open(premium_file, "r") as f:
            p_list = [l.strip() for l in f if l.strip() and not l.startswith('[')]
        selected = random.choice(p_list)
        proxies = {"http": f"http://{selected}", "https": f"http://{selected}"}
        print(f"\033[1;33m[*] Menembus via Jalur : {selected}\033[0m")
    else:
        print("\033[1;31m[!] File tidak ditemukan!\033[0m")
        return

    try:
        url = f"https://cloudflare-dns.com/query?name={domain}&type=A"
        headers = {"Accept": "application/dns-json"}
        res = requests.get(url, proxies=proxies, headers=headers, timeout=10).json()
        print(f"\n\033[1;32m[+] Hasil Intelijen DNS {domain}:\033[0m")
        if "Answer" in res:
            for record in res["Answer"]:
                print(f" -> IP Target : {record['data']}")
        else:
            print(" -> Data tidak ditemukan.")
    except Exception as e:
        print(f"\033[1;31m[!] Koneksi Gagal: {e}\033[0m")

if __name__ == "__main__":
    auto_dns()
