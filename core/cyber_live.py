import os
print("\033[1;31m[!] WORLDWIDE CYBER ATTACK MONITOR (LIVE)\033[0m")
print("[*] Stream from Global Threat Maps...")
# Simulasi stream data dari server intelijen
os.system("curl -s https://cybermap.kaspersky.com/id | head -n 1 && echo 'Connecting to Real-time Stream...'")
print("Target: USA | Type: DDoS | Intensity: HIGH")
print("Target: INDONESIA | Type: Phishing | Intensity: MEDIUM")
print("Target: CHINA | Type: Malware | Intensity: CRITICAL")
input("\nEnter...")
