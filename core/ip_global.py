import requests
print('\033[1;34m[*] YOUR GLOBAL PUBLIC IP:\033[0m')
try:
    ip = requests.get('https://api.ipify.org?format=json').json()['ip']
    print(f"IP: {ip}")
except:
    print("Gagal mengambil IP. Cek koneksi.")
