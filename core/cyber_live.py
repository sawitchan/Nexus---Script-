import requests, time, random
print("\033[1;31m[!] LIVE CYBER ATTACK STREAM (WORLDWIDE)\033[0m")
# Fetching dynamic data simulation based on real countries
targets = ["USA", "China", "Russia", "Indonesia", "Germany", "Japan"]
types = ["DDoS", "SQL Injection", "Brute Force", "Malware"]
for i in range(5):
    print(f"[*] ATTACK DETECTED: {random.choice(targets)} | TYPE: {random.choice(types)} | INTENSITY: {random.randint(70, 100)}%")
    time.sleep(0.7)