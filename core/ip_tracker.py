import requests

def track_ip():
    print("\033[1;36m[!] NEXUS-IP TRACKER\033[0m")
    target = input(" Masukkan IP Target: ")
    try:
        response = requests.get(f"http://ip-api.com/json/{target}").json()
        print(f"\n[+] Status    : {response['status']}")
        print(f"[+] Negara    : {response['country']}")
        print(f"[+] Kota      : {response['city']}")
        print(f"[+] ISP       : {response['isp']}")
        print(f"[+] Lat/Lon   : {response['lat']}, {response['lon']}")
    except:
        print("\033[1;31m[!] Gagal mengambil data IP.\033[0m")
    input("\nTekan Enter untuk kembali...")

if __name__ == "__main__":
    track_ip()
