import os, sys, time, random, requests, socket, subprocess

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"

# Stealth Infrastructure (Global DNS & Fake Headers)
GLOBAL_DNS = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222"]
STEALTH_HEADERS = [
    {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"},
    {"User-Agent": "Mozilla/5.0 (compatible; Cloudflare-Diagnostics/1.0)"},
    {"X-Forwarded-For": "8.8.8.8"},
    {"X-Real-IP": "1.1.1.1"}
]

def get_auto_proxy():
    try:
        url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all"
        proxies = requests.get(url, timeout=5).text.splitlines()
        return random.choice(proxies) if proxies else None
    except: return None

def execute_logic(mod_id, target):
    dns = random.choice(GLOBAL_DNS)
    proxy = get_auto_proxy()
    header = random.choice(STEALTH_HEADERS)
    
    log_head = f"🛰️ **NEXUS-OMNI STEALTH ACTIVE**\n"
    log_head += f"🛡️ Mode: Ghost-Identity (Google/CF)\n"
    log_head += f"🌐 DNS: {dns} | Proxy: {proxy if proxy else 'Direct'}\n"
    log_head += "─"*25 + "\n"

    # Modul 29: Stealth Port Scanner
    if mod_id == "29":
        open_ports = []
        for p in [21, 22, 80, 443, 8080]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.7)
            if s.connect_ex((target, p)) == 0: open_ports.append(str(p))
            s.close()
        res = ", ".join(open_ports) if open_ports else "Filtered/Closed"
        return f"{log_head}📍 **PORT SCAN**\nTarget: {target}\nOpen: {res}"

    # Modul 05: IP Tracker (Global Intelligence)
    elif mod_id == "05":
        try:
            r = requests.get(f"http://ip-api.com/json/{target}", headers=header, timeout=10).json()
            return f"{log_head}🌐 **IP INTEL**\nISP: {r.get('isp')}\nCountry: {r.get('country')}\nStatus: Identity Masked"
        except: return f"{log_head}❌ Gagal bypass filter target."

    return f"{log_head}⚙️ Modul {mod_id} Ready."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Season 2 (Telegram Remote)
        m_id = sys.argv[2]
        tgt = sys.argv[4]
        print(execute_logic(m_id, tgt))
    else:
        # Season 1 (Termux Visual)
        os.system('clear')
        print("\033[1;31m[!] NEXUS-OMNI V14.5 - STEALTH CORE\033[0m")
        print(">> Identity: MASKED AS GOOGLEBOT")
        print(">> Season 1 & 2 Sync: SUCCESS")
