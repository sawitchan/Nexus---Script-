import socket

print("\033[1;36m" + "="*40)
print("      NEXUS-OMNI DNS LOOKUP")
print("="*40 + "\033[0m")

domain = input("[?] Masukkan Domain (ex: google.com): ")

try:
    ip_addr = socket.gethostbyname(domain)
    print(f"\033[1;32m[+] Domain: {domain}")
    print(f"[+] IP Address: {ip_addr}\033[0m")
except socket.gaierror:
    print("\033[1;31m[!] Error: Domain tidak valid.\033[0m")

print("\033[1;36m" + "="*40 + "\033[0m")
