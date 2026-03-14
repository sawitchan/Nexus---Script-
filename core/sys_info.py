import platform, os, shutil
print("\033[1;38;5;214m╔═════════ OS SYSTEM INFORMATION ═════════╗\033[0m")
print(f"║ NODE     : {platform.node()}")
print(f"║ SYSTEM   : {platform.system()} {platform.release()}")
print(f"║ MACHINE  : {platform.machine()}")
print(f"║ STORAGE  : {shutil.disk_usage('/')[2] // (2**30)} GB Free")
print("\033[1;38;5;214m╚══════════════════════════════════════════╝\033[0m")
input("Enter untuk kembali...")
