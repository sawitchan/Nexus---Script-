import os
print("\033[1;32m[*] TOP 10 RESOURCE CONSUMING PROCESSES\033[0m")
os.system("ps -eo user,pid,pcpu,pmem,comm --sort=-pcpu | head -n 11")