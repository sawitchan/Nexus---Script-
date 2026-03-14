#!/bin/bash
clear; echo -e "\033[1;33m[*] INITIALIZING GLOBAL PROXY TUNNEL...\033[0m"
if ! pgrep -x "tor" > /dev/null; then tor > /dev/null 2>&1 & sleep 5; fi
export http_proxy="socks5://127.0.0.1:9050"; export https_proxy="socks5://127.0.0.1:9050"
echo -e "\033[1;32m[+] Nexus Tunnel Established!\033[0m"
echo -e "[*] Mengecek Lokasi Anonim..."
curl -s --socks5-hostname 127.0.0.1:9050 https://ipwho.is/ | grep -E "ip|city|country"
echo -e "\n\033[1;31m[!] Koneksi Terenkripsi.\033[0m"; read -p "Enter..."
