echo -e "\033[1;33m[*] Scanning Local Network (ARP)...\033[0m"
nmap -sn 192.168.1.0/24 | grep "Nmap scan report"
read -p "Enter..."
