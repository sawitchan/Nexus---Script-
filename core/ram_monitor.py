import os
print("\033[1;36m[*] RAM USAGE INFO\033[0m")
os.system("free -h")
# Visual Bar
used = os.popen("free | grep Mem | awk '{print $3/$2 * 100}'").read()
bar = "#" * int(float(used)/5)
print(f"Progress: [{bar:<20}] {float(used):.2f}%")