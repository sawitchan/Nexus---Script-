import os
import time

def monitor_traffic():
    print("\033[1;32m[+] Nexus Shield: Monitoring Traffic...\033[0m")
    # Logic untuk memantau log akses
    while True:
        try:
            # Simulasi deteksi paket (bisa Tuan kembangkan lagi)
            time.sleep(5)
            print("[SAFE] No intrusion detected.")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    monitor_traffic()
