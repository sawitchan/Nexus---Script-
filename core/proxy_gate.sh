#!/bin/bash
echo -e "\033[1;33m[*] STARTING TOR TUNNEL...\033[0m"
pgrep -x tor > /dev/null || (nohup tor > /dev/null 2>&1 & sleep 5)
curl --socks5-hostname 127.0.0.1:9050 -s https://ipapi.co/json/
