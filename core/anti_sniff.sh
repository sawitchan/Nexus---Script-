echo -e "\033[1;31m[*] SCANNING FOR NETWORK SNIFFERS...\033[0m"
if ps aux | grep -E "tcpdump|wireshark|tshark" | grep -v grep; then
    echo -e "\033[1;31m[!] WARNING: POTENTIAL SNIFFER DETECTED!\033[0m"
else
    echo -e "\033[1;32m[+] Network Secure. No Sniffers Found.\033[0m"
fi
read -p "Enter..."
