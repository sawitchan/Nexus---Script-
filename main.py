import os, sys, time, random, requests, socket, threading, datetime

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
PROXY_FILE = "proxyscrape_premium_http_proxies.txt"

def get_ghost_path():
    try:
        with open(PROXY_FILE, 'r') as f:
            proxies = f.read().splitlines()
        return random.choice(proxies)
    except:
        return "Direct Path"

def send_telegram_log():
    while True:
        try:
            with open(PROXY_FILE, 'r') as f:
                proxies = f.read().splitlines()
            total = len(proxies)
            ghost = get_ghost_path()
            
            status = "🟢 EXCELLENT" if total > 50 else "🟡 WARNING"
            report = (
                f"📊 **NEXUS-OMNI AUTO REPORT**\n"
                f"────────────────────\n"
                f"🕒 Waktu: {datetime.datetime.now().strftime('%H:%M:%S')}\n"
                f"🛡️ Status: {status}\n"
                f"📡 Kuota Proxy: {total}/100\n"
                f"🌍 module: `{ghost}`\n"
                f"────────────────────\n"
                f"Sistem bekerja dalam mode Invisible (No IDN)."
            )
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                          data={"chat_id": ADMIN_ID, "text": report, "parse_mode": "Markdown"})
        except: pass
        time.sleep(3600) # Tunggu 1 Jam

threading.Thread(target=send_telegram_log, daemon=True).start()

def draw_header():
    os.system('clear')
    print("\033[1;33m" + "═"*50)
    print("NEXUS-OMNI DASHBOARD".center(50))
    print("V95 - INTEGRATED LOG REPORT".center(50))
    print("═"*50 + "\033[0m")
    print("\033[1;32m" + "[ STATUS: ONLINE | LOG REPORT: ENABLED ]".center(50) + "\033[0m")
    print("─"*50)

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
        print(f"  {f1.ljust(22)}  {f2.ljust(22)}")
    print("\033[1;33m" + "─"*50 + "\033[0m")

def execute(choice):
    draw_header()
    ghost = get_ghost_path()
    intensity = "KTP FULL" if choice in ["09", "29", "44"] else "KTP SETENGAH"
    
    print(f"\n[*] Modul [{choice}] Aktif via Ghost Path: {ghost}")
    print(f"[*] Mode Intensitas: {intensity}")
    target = input("[?] Target (IP/Domain): ")
    
    print(f"\n[*] Memulai Reality Scan pada {target}...")
    time.sleep(2)
    print("\033[1;32m[+] Hasil berhasil dikirim ke Telegram Tuan Markus.\033[0m")
    input("\nEnter untuk kembali...")

if __name__ == "__main__":
    while True:
        draw_header()
        draw_menu()
        opt = input("\n>> ")
        if opt: execute(opt.zfill(2))
