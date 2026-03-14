import os
import time

FILES_TO_CLEAN = ["access.log", "core/ghost.log"]

def clean_system():
    print("\033[1;32m[*] MAINTENANCE GHOST: Cleaning temporary logs...\033[0m")
    for file in FILES_TO_CLEAN:
        if os.path.exists(file):
            with open(file, "w") as f:
                f.write("") # Mengosongkan isi file tanpa menghapus filenya
            print(f"[+] {file} has been cleared.")

if __name__ == "__main__":
    while True:
        clean_system()
        time.sleep(3600) # Jalan otomatis setiap 1 jam
