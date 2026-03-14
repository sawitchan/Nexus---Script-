import os
print("\033[1;32m[*] SMART PROCESS MONITORING\033[0m")
# Hanya menampilkan 10 proses teratas yang memakan CPU
os.system("ps -eo user,pid,pcpu,pmem,comm --sort=-pcpu | head -n 11")
input("\nEnter...")
