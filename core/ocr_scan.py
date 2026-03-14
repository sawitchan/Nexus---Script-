import os
print("\033[1;36m[*] NEXUS-OCR AI SCANNER ACTIVE\033[0m")
print("[i] Mencari file teks atau log sensitif di direktori saat ini...")
# Mencari file yang mengandung kata 'password' atau 'config'
os.system("grep -rE 'pass|key|config|user' . --color=always 2>/dev/null | head -n 10")
print("\n\033[1;32m[+] Scanning Selesai.\033[0m")
input("Enter untuk kembali...")
