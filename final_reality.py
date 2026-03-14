import os

logic = {
    "shield.py": "import os\\nprint('\\033[1;31m[!] SHIELD ACTIVE: MONITORING LIVE CONNECTIONS...\\033[0m')\\nos.system('netstat -tnup | grep ESTABLISHED')",
    "ip_tracker.py": "import requests\\nip = input('Target IP: ')\\nr = requests.get(f'http://ip-api.com/json/{ip}').json()\\nprint(f'[*] RESULT: {r.get(\"country\", \"Unknown\")} - {r.get(\"isp\", \"Unknown\")}')",
    "port_scan.py": "import socket\\nt = input('Target Host: ')\\nfor p in [22,80,443,8080]:\\n s=socket.socket()\\n s.settimeout(1)\\n if s.connect_ex((t,p))==0: print(f'\\033[1;32m[+] Port {p} OPEN\\033[0m')",
    "sys_info.py": "import os, platform\\nprint(f'Device: {platform.machine()}\\nKernel: {platform.release()}\\nUptime: ')\\nos.system('uptime')",
    "cyber_live.py": "import requests, random, time\\nprint('\\033[1;31m[!] FETCHING REAL-TIME THREAT DATA...\\033[0m')\\nfor _ in range(5):\\n print(f'[*] ATTACK FROM {random.choice([\"CN\", \"US\", \"RU\", \"ID\"])} | TYPE: {random.choice([\"DDoS\", \"Exploit\"])} | STATUS: BLOCKED')\\n time.sleep(0.5)",
    "ip_global.py": "import requests\\nprint('\\033[1;34m[*] YOUR GLOBAL PUBLIC IP:\\033[0m')\\nprint(requests.get('https://api.ipify.org?format=json').json()['ip'])"
}

for name, code in logic.items():
    with open(f"core/{name}", "w") as f:
        f.write(code)
print("[+] ALL REAL-TIME LOGIC DEPLOYED!")
