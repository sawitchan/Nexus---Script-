import requests
import time
import os

TOKEN = "8615189009:AAGge6M2BWVV0U_V89LnVuoRFTksIeBMqDE"
CHAT_ID = "8358311702"
FILE_TARGET = "blocked_ips.txt"

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
        print("\033[1;32m[+] Alert sent to Telegram!\033[0m")
    except:
        print("\033[1;31m[!] Failed to send Telegram alert.\033[0m")

def monitor_blacklist():
    print("\033[1;36m[*] TELEGRAM ALERT ACTIVE... Watching for attackers.\033[0m")
    last_count = 0
    while True:
        if os.path.exists(FILE_TARGET):
            with open(FILE_TARGET, "r") as f:
                ips = f.readlines()
            
            current_count = len(ips)
            if current_count > last_count:
                new_ip = ips[-1].strip()
                msg = f"🛡️ NEXUS-OMNI ALERT!\n⚠️ Attacker Detected!\n📍 IP: {new_ip}\n🚫 Status: BLOCKED"
                send_alert(msg)
                last_count = current_count
        time.sleep(10)

if __name__ == "__main__":
    monitor_blacklist()
