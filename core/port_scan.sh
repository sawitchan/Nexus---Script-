echo -e "\033[1;36m[*] Scanning Open Ports on Localhost...\033[0m"
nmap -v localhost | grep "open"
read -p "Enter..."
