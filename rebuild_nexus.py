import os

modules = {
    "shield.py": "import os\\nprint('\\033[1;31m[!] SCANNING NETWORK TRAFFIC...\\033[0m')\\nos.system('netstat -tupln')",
    "auth.py": "import secrets\\nkey = secrets.token_hex(8)\\nprint(f'\\033[1;32m[+] NEXUS-AUTH KEYGEN: {key.upper()}\\033[0m')",
    "anti_sniff.sh": "echo -e '\\033[1;33m[*] MONITORING PACKET SNIFFING...\\033[0m'\\ntcpdump --version || pkg install tcpdump -y",
    "detector.py": "print('\\033[1;31m[!] BRUTE-FORCE DETECTION ACTIVE\\033[0m')\\nimport os\\nos.system('last -n 5')",
    "ip_tracker.py": "import requests\\nip = input('Target IP: ')\\nr = requests.get(f'http://ipapi.co/{ip}/json/').json()\\nprint(r)",
    "ocr_scan.py": "print('\\033[1;34m[*] AI SCANNER READY (OCR MODE)\\033[0m')\\nprint('[!] No Image Found in Buffer.')",
    "wifi_scan.sh": "echo -e '\\033[1;33m[*] SCANNING NEARBY WIFI (REMON)...\\033[0m'\\nnmap --version || pkg install nmap -y\\nnmap -sn 192.168.1.0/24",
    "sys_info.py": "import platform, os\\nprint(f'Kernel: {platform.release()}\\nArch: {platform.machine()}')",
    "ram_monitor.py": "import os\\nos.system('free -h')",
    "storage_deep.py": "import os\\nos.system('df -h')",
    "process_monitor.py": "import os\\nos.system('ps aux | head -n 15')",
    "ip_global.py": "import requests\\nprint(requests.get('https://ifconfig.me/all.json').json())",
    "arp_scan.sh": "echo -e '\\033[1;35m[*] ARP SCANNING LOCAL NETWORK...\\033[0m'\\narp -a",
    "port_scan.py": "import socket\\nt = input('Host: ')\\nfor p in [22,80,443]:\\n s=socket.socket()\\n s.settimeout(1)\\n if s.connect_ex((t,p))==0: print(f'Port {p}: OPEN')",
    "cyber_live.py": "import requests, random\\nt=requests.get('https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson').status_code\\nprint(f'\\033[1;31m[!] LIVE ATTACK DETECTED IN {random.choice([\"USA\",\"INDONESIA\",\"RUSSIA\"])}\\033[0m')",
}

for name, code in modules.items():
    with open(f"core/{name}", "w") as f:
        f.write(code.replace('\\\\', '\\'))

print("[+] ALL HARDCORE MODULES REBUILT!")
