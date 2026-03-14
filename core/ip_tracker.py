import requests
ip = input('Target IP: ')
r = requests.get(f'http://ip-api.com/json/{ip}').json()
print(f"[*] RESULT: {r.get('country', 'Unknown')} - {r.get('isp', 'Unknown')}")
