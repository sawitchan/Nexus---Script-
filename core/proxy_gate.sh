#!/bin/bash
clear
echo -e "\033[1;33m[*] INITIALIZING SECURE PROXY GATEWAY (TOR)...\033[0m"
if ! pgrep -x "tor" > /dev/null; then
    nohup tor > /dev/null 2>&1 &
    sleep 5
fi
echo -e "\033[1;32m[+] Nexus Tunnel Established!\033[0m"
curl --socks5-hostname 127.0.0.1:9050 -s https://ipapi.co/json/ | python3 -m json.tool
echo -e "\n\033[1;34m[!] Your identity is now hidden behind Tor Network.\033[0m"
read -p "Enter..."
