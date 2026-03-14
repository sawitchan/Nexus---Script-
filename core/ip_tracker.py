import requests
ip = input("\033[1;33m[?] Masukkan IP Target: \033[0m")
r = requests.get(f"http://ip-api.com/json/{ip}").json()
if r['status'] == 'success':
    print(f"Country: {r['country']}\nCity: {r['city']}\nISP: {r['isp']}\nLat/Lon: {r['lat']}/{r['lon']}")
else:
    print("[!] IP Tidak Valid.")