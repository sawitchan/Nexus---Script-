import socket
target = input("[?] Target (IP/Domain): ")
ports = [21, 22, 80, 443, 8080, 3306]
print(f"[*] Scanning Ports on {target}...")
for p in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((target, p)) == 0:
        print(f"Port {p} : OPEN")
    s.close()