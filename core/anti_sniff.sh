#!/bin/bash
echo -e "\033[1;33m[*] Monitoring Active Connections (CTRL+C to Stop)...\033[0m"
echo -e "\033[1;34m      PROTO      LOCAL ADDRESS           FOREIGN ADDRESS         STATE\033[0m"
while true; do
    netstat -ant | grep ESTABLISHED | head -n 10
    sleep 2
    clear
    echo -e "\033[1;33m[*] Monitoring Active Connections (CTRL+C to Stop)...\033[0m"
done
