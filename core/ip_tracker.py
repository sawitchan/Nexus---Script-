import requests
print("\033[1;33m[*] TRACKING GLOBAL IP ADDRESS...\033[0m")
ip = requests.get('https://api.ipify.org').text
data = requests.get(f'http://ip-api.com/json/{ip}').json()
for k, v in data.items():
    print(f"\033[1;37m[+] {k.upper():10} : {v}")
input("\nEnter untuk kembali...")
