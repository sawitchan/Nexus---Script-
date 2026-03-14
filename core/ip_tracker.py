import requests; print("\033[1;33m[*] TRACKING VIA CLOUD...\033[0m")
try:
    data = requests.get('https://ipwho.is/').json()
    print(f"[+] IP: {data['ip']}\n[+] Lokasi: {data['city']}, {data['country']}\n[+] ISP: {data['connection']['isp']}")
except: print("[!] API Limit. Coba lagi nanti.")
input("Enter...")
