import socket
import concurrent.futures

print("\033[1;31m" + "="*45)
print("     NEXUS-OMNI AUTO-DETECT SCANNER")
print("     [ MODE: SCAN PINTU 1-1024 ]")
print("="*45 + "\033[0m")

target = input("[?] Masukkan Target (IP/Domain): ").strip().replace("https://", "").replace("http://", "").split('/')[0]

print(f"[*] Mengetok semua pintu di {target}...")

def scan_pintu(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            print(f"\033[1;32m[+] PINTU TERDETEKSI TERBUKA: {port}\033[0m")
        s.close()
    except:
        pass

# Kita suruh 100 pekerja buat ngetok pintu 1 sampai 1024 sekaligus!
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_pintu, range(1, 1025))

print("-" * 45)
print("[*] Selesai! Semua pintu sudah diperiksa.")
