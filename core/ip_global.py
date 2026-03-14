import requests
print("\033[1;35m[*] CAPTURING GLOBAL NETWORK INFO\033[0m")
try:
    info = requests.get('https://ipapi.co/json/').json()
    print(f"Public IP : {info['ip']}")
    print(f"Provider  : {info['org']}")
    print(f"Region    : {info['city']}, {info['country_name']}")
except: print("[!] Connection Error")
input("\nEnter...")
