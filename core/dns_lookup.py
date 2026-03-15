import requests
import random

def auto_dns():
    print("\033[1;36m" + "="*45)
    print("     NEXUS-OMNI DNS ")
    print("="*45 + "\033[0m")
    
    domain = input("[?] Masukkan Domain Target: ").strip()
    if not domain: return

    # API khusus untuk memastikan tidak ada IP IDN yang masuk
    url_api = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    try:
        res_proxy = requests.get(url_api, timeout=5).text.strip().split('\r\n')
        proxy = random.choice(res_proxy)
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        print(f"\033[1;33m[*] Melompat ke Negara Luar: {proxy}\033[0m")
        
        url_dns = f"https://cloudflare-dns.com/query?name={domain}&type=A"
        headers = {"Accept": "application/dns-json"}
        res = requests.get(url_dns, proxies=proxies, headers=headers, timeout=10).json()
        
        print(f"\n\033[1;32m[+] Hasil Intelijen DNS (Jalur Luar Negeri):\033[0m")
        for record in res.get("Answer", []):
            print(f" -> IP Target : {record['data']}")
    except:
        print("\033[1;31m[!] Gagal menembus jalur internasional.\033[0m")

if __name__ == "__main__":
    auto_dns()
