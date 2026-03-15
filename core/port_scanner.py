import socket
import requests
import concurrent.futures

print("\033[1;33m" + "═"*45)
print("     NEXUS-OMNI INTELLIGENCE SCANNER (KTP MODE)")
print("═"*45 + "\033[0m")

target = input("[?] Masukkan Target (IP/Domain): ").strip().replace("https://", "").replace("http://", "").split('/')[0]

# --- BAGIAN 1: TRACKING LOKASI (DATA KTP IP) ---
print(f"\n[*] Mengambil Data Intelijen untuk: {target}...")
try:
    response = requests.get(f"http://ip-api.com/json/{target}").json()
    if response['status'] == 'success':
        print(f"\033[1;36m[ID] Negara    : {response['country']}")
        print(f"[ID] Kota      : {response['city']}")
        print(f"[ID] ISP       : {response['isp']}")
        print(f"[ID] Lat/Lon   : {response['lat']}, {response['lon']}\033[0m")
    else:
        print("\033[1;31m[!] Data Lokasi tidak ditemukan.\033[0m")
except:
    print("\033[1;31m[!] Gagal koneksi ke database Intel.\033[0m")

print("-" * 45)

# --- BAGIAN 2: AUTO-DETECT PINTU (1-1024) ---
print(f"[*] Mencari celah pintu di {target}...")

def scan_pintu(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            print(f"\033[1;32m[+] TERDETEKSI TERBUKA: Port {port}\033[0m")
        s.close()
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_pintu, range(1, 1025))

print("-" * 45)
print("Selesai, Tuan Nexus! Data Intel & Port sudah siap.")
