import socket
from datetime import datetime

target = input("\033[1;34m[?] Masukkan Host/IP Target: \033[0m")
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Scanning started at: {str(datetime.now())}")
print("-" * 50)

ports = [21, 22, 80, 443, 3306, 8080] # Port standar yang sering dicek hacker

try:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"\033[1;32m[+] Port {port} is OPEN\033[0m")
        else:
            print(f"\033[1;31m[-] Port {port} is CLOSED\033[0m")
        s.close()
except:
    print("\n\033[1;31m[!] Error: Gagal koneksi ke target.\033[0m")

print("-" * 50)
