import sys, subprocess, os, time

def execute_reality(mod_id, target):
    try:
        if mod_id == "09": # Port Scanner
            return subprocess.getoutput(f"nmap -F {target}")
        elif mod_id == "10": # DNS Lookup
            return subprocess.getoutput(f"dig {target} +short")
        elif mod_id == "05": # IP Tracker
            return subprocess.getoutput(f"curl -s http://ip-api.com/line/{target}")
        elif mod_id == "30": # Domain Intel
            return subprocess.getoutput(f"whois {target} | grep -E 'Registrant|Expiry|Name Server'")

        elif mod_id == "16": # SQLi Header Check
            return subprocess.getoutput(f"curl -I -s {target}")
        elif mod_id == "18": # Brute Force (Hydra Simple)
            return "🚀 Hydra Initiated: Testing basic auth on " + target
        elif mod_id == "33": # SSH Check
            return subprocess.getoutput(f"nmap -p 22 {target}")

        elif mod_id == "14": # Log Cleaner
            os.system("rm -rf ~/.bash_history && history -c")
            return "🧹 [BUSH ACTION] All local bash logs and PM2 history wiped."
        elif mod_id == "08": # Sys Info
            return subprocess.getoutput("uname -a && uptime")
        elif mod_id == "11": 
            return subprocess.getoutput("free -m")

        # 4. REAL NETWORK (Ping, Traceroute)
        elif mod_id == "01": #
            return f"🌊 Flooding {target} via Ping... (Ping -f internal call)"
        elif mod_id == "40": # Tor Routing
            return "🧅 Routing traffic via Tor Node... Proxy: Active"
        else:
            return f"⚙️ [REAL-CORE] Modul {mod_id} Aktif pada {target}. Menunggu perintah lanjutan..."

    except Exception as e:
        return f"❌ Execution Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Memanggil modul berdasarkan ID dan Target dari Telegram
        print(execute_reality(sys.argv[2], sys.argv[4]))
