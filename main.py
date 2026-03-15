import os, sys, time, random, requests, subprocess

# --- CORE SETTINGS ---
TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
CORE_DIR = "./core"

def auto_dep_install(package):
    """Fitur Auto-Install Dependency jika library hilang"""
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def log_wiper():
    os.system('rm -rf ~/.pm2/logs/* && history -c')

def execute_logic(mod_id, target):
    # Mapping 50 fitur ke file di folder core
    mapping = {
        "01": "ddos_shield.sh", "03": "anti_sniff.sh", "05": "ip_tracker.py",
        "09": "port_scanner.py", "11": "ram_monitor.py", "15": "ip_global.py",
        "29": "port_scan.sh", "30": "dns_lookup.py"
    }
    
    script = mapping.get(mod_id, "sys_info.py")
    path = os.path.join(CORE_DIR, script)
    
    if os.path.exists(path):
        ext = script.split('.')[-1]
        cmd = f"python3 {path}" if ext == 'py' else f"bash {path}"
        res = subprocess.getoutput(f"{cmd} {target}")
        log_wiper()
        return f"🛰️ **NEXUS REPORT**\nModul: {mod_id}\n{res}"
    return f"❌ Modul {mod_id} ({script}) belum sinkron di /core/."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Season 2 (Telegram Remote)
        try:
            m_id = sys.argv[2].zfill(2)
            tgt = sys.argv[4]
            print(execute_logic(m_id, tgt))
        except: print("Invalid Remote Params")
    else:
        # Season 1 (Termux UI)
        os.system('clear')
        print("\033[1;32m[+] NEXUS-OMNI V15.5 FINAL ACTIVE\033[0m")
        print("[*] Stealth & Auto-Dependency: ON")
