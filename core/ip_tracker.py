import requests
ip = requests.get('https://api.ipify.org').text
data = requests.get(f'http://ip-api.com/json/{ip}').json()
print(f"[*] IP: {data['query']}\n[*] LOKASI: {data['city']}, {data['country']}")
input('Enter...')
