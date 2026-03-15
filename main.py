import os, sys, time, random, requests, subprocess

TOKEN = "8268861412:AAHo2cUeZOJx9G0H3xDegw9Cy27-3Vi3IZ0"
ADMIN_ID = "8358311702"
CORE_DIR = "./core"

def log_wiper():
    os.system('rm -rf ~/.pm2/logs/* && history -c')

def execute_core_script(script_name, target):
    """Menjalankan file spesifik dari folder core"""
    path = os.path.join(CORE_DIR, script_name)
    if os.path.exists(path):
        # Menggunakan identitas Googlebot via Environment Variable
        return subprocess.getoutput(f"export USER_AGENT='Googlebot'; python3 {path} {target}")
    else:
        return f"❌ Error: {script_name} tidak ditemukan di folder /core/"

def execute_logic(mod_id, target):
    # Mapping Modul ke File di folder /core Tuan
    mapping = {
        "05": "ip_tracker.py",
        "29": "port_scanner.py",
        "30": "dns_lookup.py",
        "15": "ip_global.py",
        "26": "intrusion_detect.py"
    }
    
    script = mapping.get(mod_id)
    if script:
        res = execute_core_script(script, target)
        log_wiper()
        return f"🛰️ **NEXUS STEALTH REPORT**\nModul: {mod_id}\nTarget: {target}\n{res}"
    
    return "⚙️ Modul sedang di-sinkronkan ulang..."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        m_id = sys.argv[2].zfill(2)
        tgt = sys.argv[4]
        print(execute_logic(m_id, tgt))
    else:
        os.system('clear')
        print("\033[1;32m[+] CORE RECOVERY SUCCESSFUL\033[0m")
        print(f"[*] Found {len(os.listdir(CORE_DIR))} Modules in /core/")
