import os, time
print("\033[1;36m[*] RESPONSIVE MEMORY MONITOR (Real-Time)\033[0m")
os.system("free -h | awk 'NR==1{print \"      \",$1,$2,$3} NR==2{print \"[MEM] \",$2,$3,$4}'")
# Grafik Sederhana
mem = os.popen("free | grep Mem | awk '{print $3/$2 * 100}'").read()
print(f"Usage: [{'#'*int(float(mem)/5)}{'-'*(20-int(float(mem)/5))}] {float(mem):.2f}%")
input("\nEnter...")
