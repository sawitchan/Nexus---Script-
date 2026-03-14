import hashlib; import time; key = hashlib.md5(str(time.time()).encode()).hexdigest().upper()[:16]
print(f"\033[1;33m[+] NEW LICENSE KEY: {key[:4]}-{key[4:8]}-{key[8:12]}\033[0m"); input("Enter...")
