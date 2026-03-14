import os, platform
print("\033[1;33m[+] DEEP DEVICE ANALYZER\033[0m")
print(f"OS Version : {platform.platform()}")
print(f"Kernel     : {platform.release()}")
print(f"Installed  : {len(os.popen('pkg list-installed').readlines())} Packages")
print("-" * 30)
os.system("df -h /data/data/com.termux/files/home")
input("\nEnter...")
