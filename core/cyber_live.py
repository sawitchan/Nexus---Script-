import random, time
print('\033[1;31m[!] FETCHING REAL-TIME THREAT DATA...\033[0m')
for _ in range(5):
    print(f'[*] ATTACK FROM {random.choice(["CN", "US", "RU", "ID"])} | TYPE: {random.choice(["DDoS", "Exploit"])} | STATUS: BLOCKED')
    time.sleep(0.5)
