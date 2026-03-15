import os, sys, time, random, requests, threading, datetime

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
PROXY_FILE = "proxyscrape_premium_http_proxies.txt"

def clear(): os.system('clear')

def get_ghost_path():
    try:
        with open(PROXY_FILE, 'r') as f:
            proxies = f.read().splitlines()
        return random.choice(proxies)
    except: return "Global-Ghost-Path"

def draw_header():
    clear()
    print("\033[1;33m" + "╔══════════════════════════════════════════════════════╗")
    print("║                NEXUS-OMNI DASHBOARD                  ║")
    print("║           V12.0 - ULTIMATE SYMMETRIC UI              ║")
    print("╚══════════════════════════════════════════════════════╝" + "\033[0m")
    print("\033[1;32m" + "[ STATUS: ONLINE | SERVER ACTIVE ]".center(54) + "\033[0m")
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
        num1 = str(i+1).zfill(2)
        num2 = str(i+2).zfill(2)
        f1 = f"[{num1}] {features[i]}"
        f2 = f"[{num2}] {features[i+1]}"
        print(f"  {f1.ljust(24)}  {f2.ljust(24)}  ")
    print("\033[1;33m" + "─"*54 + "\033[0m")

def execute_module(choice):
    draw_header()
    ghost = get_ghost_path()
    intensity = "KTP FULL" if choice in ["09", "29", "44"] else "KTP SETENGAH"
    
    print(f"\n\033[1;33m      NEXUS-OMNI INTELLIGENCE SCANNER ({intensity})\033[0m".center(54))
    print("─"*54)
    target = input("\n[?] Masukkan Target (IP/Domain): ").strip()
    
    if target:
        print(f"\n[*] Menarik Data Reality via {ghost}...")
        time.sleep(1.5)
        try:
            res = requests.get(f"http://ip-api.com/json/{target}", timeout=5).json()
            print(f"\033[1;36m[ID] Negara : {res.get('country')}\n[ID] ISP    : {res.get('isp')}\033[0m")
        except: print("[!] Jalur Proxy Sibuk.")
    
    input("\nKlik Enter untuk kembali...")

if __name__ == "__main__":
    while True:
        draw_header()
        draw_menu()
        opt = input("\n >> ").strip()
        if opt: execute_module(opt.zfill(2))
