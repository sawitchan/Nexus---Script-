import requests
import os

def scan_now():
    print("\033[1;35m[!] NEXUS-OCR AI SCANNER\033[0m")
    img_path = input(" Masukkan Path/Lokasi Gambar: ")
    
    if not os.path.exists(img_path):
        print("\033[1;31m[!] File tidak ditemukan!\033[0m")
        return

    api_key = "K83088163488957"
    url = "https://api.ocr.space/parse/image"
    
    print("[*] Mengirim data ke AI Server...")
    try:
        with open(img_path, 'rb') as f:
            r = requests.post(url, files={'image': f}, data={'apikey': api_key})
        
        result = r.json()
        text = result.get("ParsedResults")[0].get("ParsedText")
        print("\n\033[1;32m[+] HASIL SCAN:\033[0m")
        print("-" * 30)
        print(text)
        print("-" * 30)
    except:
        print("\033[1;31m[!] Gagal memproses gambar.\033[0m")
    
    input("\nTekan Enter untuk kembali...")

if __name__ == "__main__":
    scan_now()
