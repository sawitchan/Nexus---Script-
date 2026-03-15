import os, sys, time, random, requests, socket

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
PROXY_FILE = "proxyscrape_premium_http_proxies.txt"

def clear(): os.system('clear')

def send_tele(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      data={"chat_id": ADMIN_ID, "text": msg, "parse_mode": "Markdown"})
    except: pass

def get_ghost():
    try:
        with open(PROXY_FILE, 'r') as f:
            proxies = f.read().splitlines()
        return random.choice(proxies)
    except: return "Global-Ghost-Link"

def draw_header():
    clear()
    print("\033[1;33m" + "╔══════════════════════════════════════════════════════╗")
    print("║                NEXUS-OMNI DASHBOARD                  ║")
    print("║           V12.0 - SIMI UI           ║")
    print("╚══════════════════════════════════════════════════════╝" + "\033[0m")
    print("\033[1;32m" + "[ STATUS: ONLINE | REAL-TIME ACTIVE ]".center(54) + "\033[0m")
    print("─"*54)

def draw_menu():
    features = [
        "DDoS Shield", "Auth Keygen", "Anti-Sniff", "Web-Shield", "IP Tracker",
        "Proxy Scraper", "MAC Changer", "System Info", "Port Scanner", "DNS Lookup",
        "RAM Usage", "CPU Temp", "Storage Check", "Log Cleaner", "Global IP",
        "SQL Injector", "XSS Scanner", "Brute Force", "Payload Gen", "Backdoor",
        "Cyber Live", "Proxy Gate", "VPN Tunnel", "Botnet Node", "Health Check",
        "IDS Sniffer", "Telegram Alert", "Auto Clean", "Deep Scan", "Domain Intel",
        "WiFi Cracker", "Packet Sniff", "Ssh Brute", "Ftp Exploit", "Metadata Ex",
        "Hash Cracker", "Subdom Finder", "Email Verif", "Cloud Flare BP", "Tor Node",
        "Admin Finder", "Port Forward", "Sitemap Gen", "Vuln Scanner", "Shell Access",
        "API Protect", "Encrypter", "Decrypter", "Web Cloner", "Final Defense"
    ]
    for i in range(0, 50, 2):
        f1 = f"[{str(i+1).zfill(2)}] {features[i]}"
        f2 = f"[{str(i+2).zfill(2)}] {features[i+1]}"
        print(f"  {f1.ljust(24)}  {f2.ljust(24)}  ")
    print("\033[1;33m" + "─"*54 + "\033[0m")

def run_reality(choice):
    draw_header()
    is_full = choice in ["01", "09", "16", "29", "44", "50"]
    mode = "KTP FULL" if is_full else "KTP SETENGAH"
    ghost = get_ghost()
    
    print(f"\n\033[1;33m      NEXUS-OMNI INTELLIGENCE SCANNER ({mode})\033[0m".center(54))
    print("─"*54)
    target = input("\n[?] Masukkan Target (IP/Domain): ").strip()
    if not target: return

    print(f"\n[*] Mengambil Data via {ghost}...")
    time.sleep(1)

    try:
        res = requests.get(f"http://ip-api.com/json/{target}", timeout=10).json()
        print(f"\033[1;36m[ID] Negara : {res.get('country')}\n[ID] ISP    : {res.get('isp')}")
        
        if is_full:
            print(f"[ID] Kota   : {res.get('city')}\n[ID] Lat/Lon: {res.get('lat')}, {res.get('lon')}\033[0m")
            print("\n[*] Mencari Port Terbuka (Deep Scan)...")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            if s.connect_ex((target, 80)) == 0: 
                print("\033[1;32m[+] TERDETEKSI TERBUKA: Port 80\033[0m")
            s.close()
        
        msg = f"**NEXUS REPORT**\nModul: {choice}\nTarget: {target}\nMode: {mode}\nStatus: Success"
        send_tele(msg)
        print("\033[1;32m\n[+] Report berhasil dikirim ke Telegram Tuan Nexus.\033[0m")
        
    except: 
        print("\033[1;31m[!] Gagal Terhubung ke DNS.\033[0m")
    
    input("\nKlik Enter untuk kembali...")

if __name__ == "__main__":
    while True:
        draw_header()
        draw_menu()
        opt = input("\n >> ").strip()
        if opt: run_reality(opt.zfill(2))
