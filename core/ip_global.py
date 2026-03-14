import requests
print("\033[1;34m[*] CAPTURING GLOBAL NETWORK ENTRY...\033[0m")
r = requests.get("https://ifconfig.me/all.json").json()
print(f"Public IP: {r['ip_addr']}\nUser-Agent: {r['user_agent']}")