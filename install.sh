#!/bin/bash
echo -e "\033[1;36m[*] Installing Dependencies...\033[0m"
pkg install python git make curl -y
pip install requests
chmod +x core/scripts/menu.sh
echo -e "\033[1;32m[+] Done! Type 'make run' to start.\033[0m"
