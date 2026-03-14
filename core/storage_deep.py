import os, platform
print("\033[1;33m[+] DEEP STORAGE & DEVICE INFO\033[0m")
print(f"Kernel: {platform.release()}")
print(f"Platform: {platform.platform()}")
os.system("df -h /data/data/com.termux/files/home")